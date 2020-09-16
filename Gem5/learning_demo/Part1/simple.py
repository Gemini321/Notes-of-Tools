import m5
from m5.objects import *

system = System() # 实例化一个系统

# 实例化部件

system.clk_domain = SrcClockDomain() # 设置时钟域
system.clk_domain.clock = '1GHz' # 频率
system.clk_domain.voltage_domain = VoltageDomain() # 默认电压域

system.mem_mode = 'timing' # 计时模式进行内存模拟（特殊情况除外）
system.mem_ranges = [AddrRange('512MB')] # 单个512MB内存
system.cpu = TimingSimpleCPU() # 最简单的计时CPU

# 创建总线与端口连接

system.membus = SystemXBar() # 创建内存总线

system.cpu.icache_port = system.membus.slave # 将icache和dcache直接连接到内存总线
system.cpu.dcache_port = system.membus.slave

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