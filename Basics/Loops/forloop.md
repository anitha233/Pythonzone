In Python,there are two types of loops "for" and "while"
* In "for" loop, iterate over each sequence(list,tuple,string or range) to execute for each item in sequence.

Syntax:
```python
for variable in sequence:
    # Code to be executed for each item in the sequence
```

Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```
* In "while" loop,continues to execute the block of code as long as specific condition is `True`
  
Syntax:
```python
while condition:
    # Code to be executed as long as the condition is true
```

Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1

```
### Usecases
1. Server Provisioning and Configuration
   
* We use for loops for provisioning multiple servers or virtual machine with same configuration.For example, when setting up monitoring agents on multiple servers.

```python
servers = ("server1","server2","server3")
for server in "${servers[@]}"; do
configure_monitoring_agents "$server"
done
```

1. Deploying Configurations to Multiple Environments

* When deploying configurations to different environments (e.g., development, staging, production).

```python
environments=("dev" "staging" "prod")
for env in "${environments[@]}"; do
    deploy_configuration "$env"
done
```