#CodeVs-cli
***

 欢迎使用 CodeVs-cli。
 CodeVs-cli 是一个命令行工具，它能够帮助你处理大量写程序时会遇到的琐事，从而使您能够更加专注于您的代码，逻辑和算法。您所需要额外做的事情就是看完这篇教程，然后用 CodeVs-cli 完成一道题。
 
 我们将通过编译一个用c语言写的简单目录选择程序来学习如何使用 CodeVs-cli 。
  
 ***

###Normal way: build or run

  一般情况下，您应该将所有代码放在 src 文件夹中，像这样：
><pre>/yourproject
>  |------ /src
>            |------ main.c
>            |
>            |------ /lib
>            |          |------ inputlib.c
>            |          |------ menu.c
>            |          |------ str.c
>            |
>            |------ /head
>                        |------ mpsss_inputlib.h
>                        |------ mpsss_menu.h
>                        |------ mpsss_strlib.h</pre>
  
而您之后所需要做的事情就是：

  * 打开 terminal
  * 输入 `codevs build /path/to/yourproject`
 
您可以输入绝对路径也可以是相对如今，但是最好不要是 “/path/to/yourproject” 这行字~~当年我曾犯过这样的错误 T _ T~~。然后，您会发现一个可执行文件 Main 出现在您的项目文件目录中。
使用以下命令，您就可以运行你的程序：
 		
 	$ /path/to/yourporject/Main		--your_arguments

但是，不要把 '$' 输进 terminal，那名不是命令的一部分，它只是提示您，它在等待您输入命令。同样，不要真的输入 "--your_arguments" ，那只是代表您的程序所需要的参数。

如果您觉得这样太麻烦，您或许需要 `run` 命令 ( **如果不需要和程序进行交互** ) 。

	codevs run /path/to/yourproject
	
这个命令帮您 build 项目，并且直接执行它，但是要注意，您应该把所有代码放在 src 文件夹中。

***

###Magical Way: makefile

在这种方法中，你不一定需要把所有代码都放在 src 文件夹中，但是你需要额外写一个 makefile 文件在你的项目中。

目录就像是这样：

><pre>/yourproject
>|------ main.c
>|------ makefile
>|------ /lib
>|          |------ inputlib.c
>|          |------ menu.c
>|          |------ str.c
>|
>|------ /head
>           |------ mpsss_inputlib.h
>           |------ mpsss_menu.h
>           |------ mpsss_strlib.h</pre>

如上结构，makefile文件内容是：

```makefile
menu: main.o, inputlib.o, menu.o, str.o
	gcc $^ -o $@
	rm -f *.o
main.o: main.c
	gcc -c $<
inputlib.o: ./lib/inputlib.c
	gcc -c $<
menu.o: ./lib/menu.c
	gcc -c $<
str.o: ./lib/str.c
	gcc -c $<
```

准备完了 makefile , 您只要使用命令：

	codevs make
	
您就能完成 makefile 中定义的所有命令。

想了解更多关于 makefile 的信息，请点这里

* [goolge](https://www.google.com.hk/#newwindow=1&safe=strict&q=makefile)
* [baidu](https://www.baidu.com/s?ie=utf-8&fr=bks0000&wd=Makefile)

***

如果您想要更多信息，您可以使用命令：

	codevs --help

***

<small>&copy;CodeVS</small>&nbsp;&nbsp;&nbsp;&nbsp;<span>lovely by wph95, mpsss and CodeVsers</span>



