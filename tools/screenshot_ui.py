# coding: gbk
#
import uiautomator2 as u2

d = u2.connect('bc5a8356')

im = d.xpath('//*[@resource-id="com.yiwuzhibo:id/liveroom_im_list"]/android.view.ViewGroup[8]').screenshot()
im.save(r'D:\workspace_new\uiauto2_ele\aseert_pic\test_pic.jpg')
