# 导入所需的库
import mediapipe as mp  # 使用mediapipe库进行手部识别
import cv2  # 使用OpenCV库进行图像处理


# 配置mediapipe
hand_drawing_utils = mp.solutions.drawing_utils  
#drawing_utils模块是库中专门用于绘制图像的工具模块。它提供了一些函数，可以帮助我们在图像上绘制手部关键点和连接线。
#创建了一个指向模块的引用：mp.solutions.drawing_utils
#通过将赋值给变量，我们可以使用更短的名称来引用模块。这种方式使得我们在代码中使用更加简洁方便。
#这一行代码的目的是为后续的图像绘制操作提供方便的调用方式。通过使用，我们可以更轻松地调用库中的绘图函数来绘制手部关键点和连接线。


mp_hands = mp.solutions.hands  
# 手部识别api
#对于这一行而言，其基本的原理和上面一句一模一样


my_hands = mp_hands.Hands()  
# 创建手部识别对象
#在通过Hands类实例化Hands对象时，可以通过传递参数来配置手部姿势识别的行为，在这个例子中，没有提供额外的配置参数，因此使用了默认配置。

#mp_hands.Hands()类的默认配置如下：

#model_complexity参数指定了用于手部姿势识别的模型的复杂度级别，有三个选项可供选择：
#0：较小的模型复杂度，但识别准确性可能较低；
#1：默认设置，适度的模型复杂度和识别准确性；
#2：较大的模型复杂度，能够提供更高的识别准确性，但可能会牺牲一些性能。
    #在默认情况下，就是0。也就是说如果你对手势识别的准确性要求较高，可以选择较大的模型复杂度级别，但需要牺牲一些性能。如果你在资源受限的环境下工作，可以选择较小的模型复杂度级别，但要注意准确性可能会稍有降低

#static_image_mode（静态图像模式）：默认为False。当设置为True时，方法会以静态图像模式处理输入图像，而不是连续的视频流。process()
#max_num_hands（最大手的数量）：默认为2。指定要检测的最大手的数量。
#min_detection_confidence（最小检测置信度）：默认为0.5。指定检测到的手是否可靠的置信度阈值。低于此阈值的检测结果将被过滤掉。
#min_tracking_confidence（最小跟踪置信度）：默认为0.5。指定跟踪手是否可靠的置信度阈值。低于此阈值的跟踪结果将被过滤掉。
#可以根据具体需求，通过调整这些参数的值来过滤掉置信度较低的手部检测和跟踪结果。较高的置信度阈值可以提高结果的可靠性，但也可能过滤掉一些正常的手部姿势。相反，降低置信度阈值可以保留更多的结果，但可能会引入一些不准确的结果

#如果要修改上述参数，可以在创建对象时，通过传递参数来进行配置。例如，举例代码格式如下所示
#my_hands = mp_hands.Hands(static_image_mode=True, 
#                         max_num_hands=3, 
#                        min_detection_confidence=0.7, 
#                       min_tracking_confidence=0.8，
#                       model_complexity=1)


# 打开摄像头，参数0表示默认摄像头
cap = cv2.VideoCapture(0)
#这行代码创建了一个对象，用于从摄像头捕获实时视频流。cv2.VideoCapture是OpenCV库中用于从视频源（如摄像头、视频文件等）捕获视频帧的类。
#除了传递作为参数表示默认的摄像头设备之外，还可以使用其他参数来指定不同的视频源。
#其他参数1：文件路径：可以传递一个视频文件的路径作为参数，指定要从文件中读取视频。如cap = cv2.VideoCapture("path/to/video.mp4")这将会从指定路径的视频文件中读取视频帧。
#其他参数2：视频捕获设备索引：当有多个摄像头设备时，可以传递设备的索引号来指定要使用的设备。一般情况下，索引号从0开始，表示第一个可用的摄像头设备如cap = cv2.VideoCapture(1)
#除了整数索引，还可以使用字符串类型的参数指定特定的视频源，如：
#"cam_id=0"：表示使用索引为0的摄像头设备。
#"http://example.com/live/stream"：表示从网络摄像头的实时视频流中读取视频帧。


# 通过循环读取每一帧图像
while True:
    # 从摄像头读取一帧图像
    success, img = cap.read()
    #success, img = cap.read()是OpenCV库中用于从对象cap（cv2.VideoCapture类）中读取视频帧的方法。
    #success：一个布尔值，表示是否成功读取到视频帧。如果成功读取到帧，则为True；否则为False
    #img：当前读取到的视频帧。
    #在使用对象进行视频捕获时，通常需要在一个循环中反复调用，以连续地读取视频帧。
    #在读取到帧后，可以对其进行后续处理，例如图像处理、对象检测等。

    # 检查摄像头是否成功打开
    if not success:
        print('摄像头打开失败')
        break
    #没啥说的，没打开就蹦个提示然后break出去接销毁步骤
    

    # 将BGR图像转换为RGB格式，因为mediapipe库使用RGB格式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)是OpenCV库中用于颜色转换的函数。
    #这行代码的作用是将图像从BGR颜色空间转换为RGB颜色空间。
    #img：要进行颜色转换的图像。
    #cv2.COLOR_BGR2RGB：表示颜色转换的类型。此处用于将图像从BGR（蓝绿红）颜色空间转换为RGB（红绿蓝）颜色空间。
    #在OpenCV中，图像默认采用BGR颜色顺序，但在许多其他库和应用中（如Matplotlib），使用的是RGB颜色顺序。因此，可能需要在不同的上下文中使用不同的颜色空间。
    #该函数直接对原始图像进行修改，不会返回新的图像副本。
    #要根据具体需求进行颜色空间转换，可以使用其他颜色空间转换的选项，如cv2.COLOR_RGB2GRAY来进行RGB到灰度图像的转换。
    
    
    # 使用mediapipe库识别图像中的手势，并返回结果
    results = my_hands.process(img)
    #results = my_hands.process(img)这行代码在上述代码中用于对图像进行手部识别，并将结果保存在 results变量中。
    #process()是Hands类中的一个方法，用于对输入的图像进行手部识别。它接受一个图像作为参数，并返回一个包含手部检测结果的对象。
    #此方法会返回一个包含手部识别结果的对象，其中包含了识别到的手部的相关信息，如手部关键点坐标、手势分类等。可以通过访问result对象的属性和方法来获取手部识别结果的具体信息。
    #通过处理results对象，你可以根据实际需求使用手部识别结果进行后续操作，比如图像绘制、手势分类、姿态分析等。


    # 将RGB图像转换回BGR格式，以便使用OpenCV绘制图像
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #跟刚才所说的一样的道理，把颜色格式转化回来


    # 判断是否检测到手部关键点
    if results.multi_hand_landmarks:
        #results.multi_hand_landmarks是结果对象的一个属性，它表示识别到的多个手部的关键点坐标。如果至少检测到了一个手部的关键点，则该属性的值为非空（非 None）。
        #因此， 表示如果检测到了手部关键点，则执行代码块内的操作。
        #这个条件语句的作用是确保只在检测到手部关键点时执行相关的代码，以防止对不存在的手部进行处理而导致错误。
        
        
        # 遍历每个检测到的手
        for hand_landmark in results.multi_hand_landmarks:
            #results.multi_hand_landmarks它实际上是一个列表，但更准确地说，是一个包含多个手部关键点坐标的列表。每个元素代表一个检测到的手部关键点列表，其值是一个包含关键点坐标的列表。
            #用python的for语法逐个提取
            
            
            # 使用mediapipe的绘图工具绘制手部关键点和连接线
            hand_drawing_utils.draw_landmarks(img,
                                              hand_landmark,
                                              mp_hands.HAND_CONNECTIONS,
                                              mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                                              mp.solutions.drawing_styles.get_default_hand_connections_style())
            #hand_drawing_utils.draw_landmarks()是一个用于绘制手部关键点和连接线的函数。它接受一些参数来指定要绘制的图像、手部关键点、连接线以及绘制风格等信息。
            #img：要绘制手部关键点和连接线的图像。
            #hand_landmark：一个包含手部关键点坐标的列表，表示一个检测到的手部的关键点信息。
            #mp_hands.HAND_CONNECTIONS：Hand Landmark 的连接关系，指定了手部关键点之间的连接关系。
            #mp.solutions.drawing_styles.get_default_hand_landmarks_style()：获取默认的手部关键点绘制风格。
            #mp.solutions.drawing_styles.get_default_hand_connections_style()：获取默认的手部连接线绘制风格。
            #通过调用这个函数，可以将检测到的手部关键点和手势连接线绘制在图像上，以便可视化手势识别的结果。
            #需要注意的是，在这段代码中，通过一个 for 循环遍历了results.multi_hand_landmarks 列表中的每个hand_landmark（是列表） ，然后分别对每个手部进行绘制操作。

    # 左右镜像翻转图像，使得图像在显示时更符合自然习惯（左右镜像问题）
    img = cv2.flip(img, 1)
    #img = cv2.flip(img, 1)是OpenCV库中用于图像翻转的函数。
    #这行代码的作用是对图像进行水平翻转。
    #img：要进行翻转的图像，通常是通过cv2.imread()或其他方式读取的图像。
    #1：表示翻转操作的类型。值为1时，表示水平翻转；值为0时，表示垂直翻转；值为-1时，表示水平和垂直同时翻转。
    
    
    # 在窗口中显示图像
    cv2.imshow("frame", img)
    #cv2.imshow("frame", img)是OpenCV库中用于在窗口中显示图像的函数。
    #"frame"：窗口名称，用于唯一标识要显示的窗口。可以自定义窗口名称，以便更好地区分不同的窗口。
    #img：要显示的图像。图像可以是NumPy数组形式的图像数据


    # 检测键盘输入，如果按下 'q' 键则退出循环
    key = cv2.waitKey(1) & 0xFF
    #key = cv2.waitKey(1) & 0xFF是OpenCV库中的一个函数，用于等待用户输入键盘按键，并返回用户按下的键的ASCII码值。
    #在处理视频、图像或实时摄像头捕获时，我们有时需要等待用户按下键盘上的某个键，以便执行特定的操作。cv2.waitKey()函数可以实现这一功能。
    #里面的参数1：表示等待按键的时间（单位为毫秒）。在这个时间内，会等待用户按键。如果设置为0，则表示持续等待键盘输入。
    #0xFF：这是一个掩码，用来提取按键返回值的低8位，以消除可能的影响。
    
    
    if key == ord('q'):
        break
    #ord('q')：这个语句将字符 'q' 转换为对应的 ASCII 码值。而if key == ord('q'):是一个条件语句，用于判断用户按下的键是否等于字符 'q' 的 ASCII 码值。
    #如果用户按下的键与 'q' 相匹配，则执行语句块中的代码，即break出循环并退出程序
    
    
# 释放摄像头资源
cap.release()
#这是一个定义在类里的函数，被对象调用了
#具体来说，cap.release()方法会执行以下操作：
#停止视频捕获，释放与摄像头的连接。
#关闭与摄像头设备的连接。
#释放摄像头占用的系统资源。
#注意：在使用完摄像头后，及时调用是良好编程实践，以确保及时释放摄像头资源，避免资源泄露和系统占用。
#在调用之后，就无法再通过对象进行视频捕获了。如果再次需要访问摄像头，需要重新创建一个新的对象。


# 关闭所有OpenCV窗口
cv2.destroyAllWindows()
#cv2.destroyAllWindows()是OpenCV库中用于关闭所有已经创建的窗口的函数。
#在使用OpenCV显示图像或视频时，通常会创建一个或多个窗口来展示图像或视频帧。cv2.destroyAllWindows()的作用是关闭所有这些已创建的窗口。
#这个函数通常在程序的最后用于确保在程序退出时关闭所有窗口。如果窗口没有被显式关闭，它们可能会在程序结束后继续存在，导致不必要的资源占用。    
#需要注意的是，只关闭由OpenCV创建的窗口，如果使用其他 GUI 工具库（如 Tkinter、Qt 等）创建的窗口，需要使用相应的方法来关闭这些窗口。    
    

 #mediapipe总述
 #google search 开发的一款开源的跨平台多媒体的机器学习模型应用框架
 #服务器 移动平台 嵌入式（Google coral和树莓派）
 #只需要下载一个mediapipe,所有的模型就都加载好了可以直接使用简单  
 #MediaPipe是和opencv包嵌合使用的，从官网上下载容易版本不兼容，所以尽量使用pip
 #依赖包有protobuf  opencv_contrib_python（wheel包丢了……………………）
