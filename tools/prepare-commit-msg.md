# 问题描述

工作中经常会遇到将**测试分支**或者**其它开发分支**合并到特性分支或者待上线的分支上，导致带入了一些脏代码

此类问题重复发生，不能仅仅依靠个人意识完全避免，一堆复杂的git操作操作之后，很可能会产生一些误操作，可能当事人都记不清当时具体的操作了。所以有必要使用工具进行校验，给出提示并强制终止此类误操作。

## 使用prepare-commit-msg勾子

hook脚本存放在`.git/hooks`目录下

使脚本生效只需要将对应的脚本名中的`.sample`删掉即可

脚本支持Ruby、Python语言，这里使用的Python

很简单，只需一步：

拷贝[prepare-commit-msg](https://github.com/ninemilli-song/python-garden/blob/master/tools/prepare-commit-msg)到对应工程的`.git/hooks`目录下


