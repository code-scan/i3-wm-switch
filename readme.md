### 快捷键绑定

```bash

bindsym $mod+1 exec python ~/.config/script/i3-switch.py 1
bindsym $mod+2 exec python ~/.config/script/i3-switch.py 2
bindsym $mod+3 exec python ~/.config/script/i3-switch.py 3
bindsym $mod+4 exec python ~/.config/script/i3-switch.py 4
bindsym $mod+5 exec python ~/.config/script/i3-switch.py 5
bindsym $mod+6 exec python ~/.config/script/i3-switch.py 6
bindsym $mod+7 exec python ~/.config/script/i3-switch.py 7
bindsym $mod+8 exec python ~/.config/script/i3-switch.py 8
bindsym $mod+9 exec python ~/.config/script/i3-switch.py 9
bindsym $mod+0 exec python ~/.config/script/i3-switch.py 10

```

```bash
# 获取workspace 列表 "focused": true,

i3-msg -t get_workspaces|jq


# con_id 获取 (所有窗口列表)
i3-msg -t get_tree|jq

# 使用con_id 切换焦点

i3-msg  "[con_id=94415260542592]" focus


```

### 实现逻辑

先使用`get_workspaces`获取当前focus的空间/容器num,再通过`get_tree`获取所有的窗口列表,并提取出对应num的所有窗口id

最后使用`focus`指令切换到指定的id窗口

## 参考资料
[GitHub - cornerman/i3-easyfocus: Focus and select windows in i3](https://github.com/cornerman/i3-easyfocus)

[i3: i3 User’s Guide](https://i3wm.org/docs/userguide.html#list_of_commands)

[i3-msg man page - i3 - General Commands | ManKier](https://www.mankier.com/1/i3-msg)
