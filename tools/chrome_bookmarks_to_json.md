将chrome书签转换为json格式

1. 先将chrome导出书签，导出后为html文件

> 书签 -> 书签管理器 -> 整理（右侧三个小点）-> 导出书签

2. 执行命令，将html书签转换为json

```bash
> python ./tools/chrome_bookmarks_to_json.py <your-html path>
```

# Change Log

## 2024/2/23

生成唯一id：

1. snowflake 雪花算法生成id
twitter的开源库，可以生成唯一id，有利于复杂系统的数据库检索

2. uuid
```python
import uuid
uuid = str(uuid.uuid1())
```