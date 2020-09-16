# -*- coding:UTF8 -*-
import m5
from m5.objects import *
from caches import *

from optparse import OptionParser

# 命令行参数

parser = OptionParser()
parser.add_option('--l1i_size', help="L1 instruction cache size")
parser.add_option('--l1d_size', help="L1 data cache size")
parser.add_option('--l2_size', help="Unified L2 cache size")

options, agrs = parser.parse_args()

system = System() # 实例化一个系统

# 实例化部件

system.clk_domain = SrcClockDomain() # 设置时钟域
system.clk_domain.clock = '1GHz' # 频率
system.clk_domain.voltage_domain = VoltageDomain() # 默认电压域

system.mem_mode = 'timing' # 计时模式进行内存模拟（特殊情况除外）
system.mem_ranges = [AddrRange('512MB')] # 单个512MB内存
system.cpu = TimingSimpleCPU() # 最简单的计时CPU

system.cpu.icache = L1ICache(options) # L1 icache和dcache
system.cpu.dcache = L1DCache(options)
system.cpu.l2cache = L2Cache(options) # L2 cache

# 创建总线与端口连接

system.membus = SystemXBar() # 创建内存总线

# system.cpu.icache_port = system.membus.slave # 将icache和dcache直接连接到内存总线
# system.cpu.dcache_port = system.membus.slave

system.cpu.icache.connectCPU(system.cpu) # 将icache和dcache连接到CPU
system.cpu.dcache.connectCPU(system.cpu)

system.l2bus = L2XBar()  # 创建L2总线，连接icache和dcache（L2无法直接连两个L1端口）
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.cpu.l2cache.connectCPUSideBus(system.l2bus) # 将L2连接到L2总线和内存总线
system.cpu.l2cache.connectMemSideBus(system.membus)

system.cpu.createInterruptController() # 创建中断端口（X86特殊要求）
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# 创建进程

process = Process()
process.cmd = ['tests/test-progs/hello/bin/x86/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()

print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))