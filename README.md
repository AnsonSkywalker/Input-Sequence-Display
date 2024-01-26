# Input-Sequence-Display
一个在OBS内以滚动序列形式显示用户键盘输入的脚本。A script that displays the user's keyboard input in a scrolling sequence within OBS.

使用教程：

1. 下载获取脚本文件Input_Sequence_Display.py，Clone仓库亦或者只是手动复制粘贴Python源代码均可。为了方便管理，建议将脚本文件存放在OBS的默认脚本存放路径中（..\obs-studio\data\obs-plugins\frontend-tools\scripts）
2. 启动OBS，在场景中添加一个文本源
3. 在OBS顶部工具栏中由“工具”栏进入“脚本”
4. 在脚本窗口的左下角点击“添加脚本”图标
5. 在右侧配置区域选择此文本源以将脚本和文本源绑定在一起
6. 在来源编辑器中点击“设置”以编辑文本源，在弹出的编辑窗口中勾选“聊天模式”复选框
7. 按照你的需求自行编辑文本源的其他项目。如果需要在不重启OBS的前提下将序列显示重置回初始状态，请在“脚本”工具窗口左下角点击“重新载入脚本”图标

The English version is directly translated from Chinese, so I cannot guarantee that the interface text shown in the guide is the same as the actual English version of the OBS interface text.

Usage:

1. Download the script file Input_Sequence_Display.py, no matter you want to Clone the repository or just copy and paste the source code manually. For ease of management, it is recommended to store the script file in the default script storage path of OBS (..\obs-studio\data\obs-plugins\frontend-tools\scripts).
2. Start OBS and add a text source to the scene.
3. Click on "Tools" in the toolbar at the top of OBS, then click on "Scripts".
4. Click the "Add Script" icon in the lower left corner of the Scripts window.
5. Select the text source in the right configuration area to bind the script to the text source, and then close the Scripts window to return to the main OBS interface.
6. In the source editor, select the text source you just bind and right-click the source and "Settings" to edit the source, then click the "Chat Mode" checkbox in the pop-up editing window.
7. Edit other items of the text source according to your needs. If you need to reset the sequence display back to its default state without restarting OBS, please click the "Reload Script" icon in the lower left corner of the "Scripts" tool window.
