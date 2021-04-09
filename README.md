# A forked & modified version of https://github.com/Star-Clouds/CenterFace that fit in `dhp` project

## INSTALL

```bash
python -m pip install .
```

## Example
```python
from centerface import CenterFace

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w = frame.shape[:2]
centerface = CenterFace(landmarks=True) # default
while True:
    ret, frame = cap.read()
    dets, lms = centerface(frame, h, w, threshold=0.35)
    for det in dets:
        boxes, score = det[:4], det[4]
        cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)
    for lm in lms:
        for i in range(0, 5):
            cv2.circle(frame, (int(lm[i * 2]), int(lm[i * 2 + 1])), 2, (0, 0, 255), -1)
    cv2.imshow('out', frame)
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
```

## Author
 - [ywlife](https://github.com/ywlife)
 - [SyGoing](https://github.com/SyGoing)
 - [MirrorYuChen](https://github.com/MirrorYuChen)

##  Citation
If you benefit from our work in your research and product, please consider to cite the following related papers:
```
@inproceedings{CenterFace,
title={CenterFace: Joint Face Detection and Alignment Using Face as Point},
author={Xu, Yuanyuan and Yan, Wan and Sun, Haixin and Yang, Genke and Luo, Jiliang},
booktitle={arXiv:1911.03599},
year={2019}
}
```
