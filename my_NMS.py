def my_NMS(dets, iou_thres=0.6, score_thresh, sigma, method=1):
    	'''
	Arguments:
		prediction {[tensor]} -- (x,y,w,h,conf,cls)
	
	Keyword Arguments:
		iou_thresh {number} -- [description] (default: {0.6})
	'''
	x1 = dets[:,0]
	y1 = dets[:,1]
	x2 = dets[:,2]
	y2 = dets[:,3]
	scores = dets[:,4]
	#每一个检测框的面积
	areas = (x2-x1) *(y2-y1)
	N = prediction.shape[0]
	for i in range(N):
    	cur_box = dets[i, :4].copy()
		cur_score = scores[i].copy()
		cur_area = areas[i].copy()
		pos = i+1

		if i != N-1:
    		maxScore = np.max(scores[pos:], axis = 0)
			maxPos = np.argmax(scores[pos:], axis = 0)
		else:
    		maxScore = scores[-1]
			maxPos = 0
		
		if cur_score < maxScore: #说明当前框不是排序最大的
			dets[i, :] = dets[maxPos+i+1, :]
			dets[maxPos + i + 1, :4] =  cur_box
			cur_box = dets[i, :4]

			scores[i] = scores[maxPos + i + 1]
			scores[maxPos + i + 1] = cur_score
			cur_score = scores[i]

			areas[i] = areas[maxPos + i + 1]
			areas[maxPos + i + 1] = cur_area
			cur_area = areas[i]

		#IOU的计算
		xx1 = np.maximum(dets[i, 0], dets[pos:, 0])
		yy1 = np.maximun(dets[i, 1], dets[pos:, 1])
		xx2 = np.maxinum(dets[i, 2], dets[pos:, 2])
		yy2 = np.maximum(dets[i, 3], dets[pos:, 3])

		w = np.maximum(0.0, xx2 - xx1)
		h = np.maximum(0.0, yy2 - yy1)
		inter = w * h
		ovr = inter / (areas[i] + areas[pos:] - inter)

		if method == 1:
    		weight = np.ones(ovr.shape)
			weight[ovr > iou_thres] = weight[ovr > iou_thres] - ovr[ovr > iou_thres]
		elif method == 2:
    		weight = np.exp(-(ovr*ovr)/sigma)
		else:
    		weight = np.ones(ovr.shape)
			weight[ovr> iou_thres] = 0
		scores[pos:] = weight * scores[pos:]
	inds = dets[:, 4][scores > score_thresh]
	keep = inds.astype(int)
	return keep

def weighted_nms(dets, thresh=0.5):
    	x1 = dets[:,0]
		y1 = dets[:,1]
		x2 = dets[:,2]
		y2 = dets[:,3]
		scores = dets[:,4]
		areas = (x2 - x1 + 1) *(y2-y1+1)
		order = scores.argsort()[::-1]

		keep = []
		weighted_boxes = []
		while order.size() > 0:
    			i = order[0]
				keep.append(i)
				xx1 = np.maximum(x1[i], x1[order[1:]])
				yy1 = np.maximum(y1[i], y1[order[1:]])
				xx2 = np.maximum(x2[i], x2[order[1:]])
				yy2 = np.maximum(y2[i], y2[order[1:]])

				w = np.maximum(0.0, xx2 - xx1)
				h = np.maximum(0.0, yy2 - yy1)
				inter = w * h
				iou = inter / (areas[i] + areas[order[1:]] - inter) 

				#超过阈值的
				in_inds = np.where(iou >= threshold)[0]
				in_dets = dets[inds,:]
				weights = in_dets[:, 4] * iou[in_inds]
				wbox = np.sum((in_dets[:,:4]*weights[...,np.newaxis]), axis=0)/np.sum(weights)
				weighted_boxes.append(wbox)

				#没有超过阈值的
				out_inds = np.where(iou < threshold)[0]
				order = order[out_inds]
				dets = dets[out_inds]
		return keep, np.array(weighted_boxes)



# 灰度处理
cv_img = cv2.imdecode(filePath,cv2.IMREAD_COLOR)
cv_img = cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)

# 或者是
cv_img = cv2.imread(filePath,cv2.IMREAD_COLOR) # BGR
gray = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)

#二值化处理，是通过cv.Threshold()对经过灰度化的图像进行处理
ret, binary = cv2.threshold(img_gauss,127,255, cv2.THRESH_BINARY_INV)





#各种滤波处理
img = cv2.imread(filename)
 # * src：图像矩阵
 # * ksize：滤波窗口尺寸
img_blur = cv2.blur(img, 11) #均值滤波


# * src：图像矩阵
# * ksize：滤波窗口尺寸
img_medianblur = cv2.medianBlur(img, 11) #中值滤波

#* src：图像矩阵
# * d：邻域直径
# * sigmaColor：颜色标准差
# * sigmaSpace：空间标准差
img_bilateralblur = cv2.bilateralFilter(img, 9, 5, 5) # 双边滤波


# * src: 图像矩阵
# * ksize: 滤波窗口尺寸
# * sigmax: 标准差
img_Gaussianblur = cv2.GaussianBlur(img, (3,3), 0),







if __name__ == '__main__':
    import torch
    prediction = torch.Tensor((32, 7)) #假设有两个类
    from IPython import embed
    embed()
    pass

