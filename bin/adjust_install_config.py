#!/bin/python
import yaml;
path = "install-config.yaml";
data = yaml.safe_load(open(path));
data["compute"][0]["replicas"] = 0;
data["networking"]["machineNetwork"][0]["cidr"] = "192.0.2.0/24";
open(path, "w").write(yaml.dump(data, default_flow_style=False))
