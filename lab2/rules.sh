#!/bin/sh

# http h1-a-b-d-h2
ovs-ofctl add-flow s1 in_port=1,priority=65535,tcp_dst=80,actions=output:2
ovs-ofctl add-flow s2 in_port=1,priority=65535,tcp_dst=80,actions=output:2
ovs-ofctl add-flow s4 in_port=1,priority=65535,tcp_dst=80,actions=output:2

# non http h1-a-c-e-d-h2
ovs-ofctl add-flow s1 in_port=1,actions=output:3
ovs-ofctl add-flow s3 in_port=1,actions=output:2
ovs-ofctl add-flow s5 in_port=1,actions=output:3
ovs-ofctl add-flow s4 in_port=4,actions=output:2

# http h2-d-c-a-h1
ovs-ofctl add-flow s4 in_port=2,priority=65535,tcp_dst=80,actions=output:3
ovs-ofctl add-flow s3 in_port=3,priority=65535,tcp_dst=80,actions=output:1
ovs-ofctl add-flow s1 in_port=3,priority=65535,tcp_dst=80,actions=output:1

# non http h2-d-b-e-c-a-h1
ovs-ofctl add-flow s4 in_port=2,actions=output:1
ovs-ofctl add-flow s2 in_port=2,actions=output:3
ovs-ofctl add-flow s5 in_port=2,actions=output:1
ovs-ofctl add-flow s3 in_port=2,actions=output:1
ovs-ofctl add-flow s1 in_port=3,actions=output:1