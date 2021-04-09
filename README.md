# A forked & modified version of https://github.com/Star-Clouds/CenterFace that fit in `dhp` project

## INSTALL

TL;DR:
```bash
python -m pip install .
```

Details:
``` bash
$ cd <centerface directory>
$ <activate your python environment>
$ python -m pip install .
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
        box, score = det[:4], det[4]
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (2, 255, 0), 1)
    for lm in lms:
        for i in range(0, 5):
            cv2.circle(frame, (int(lm[i * 2]), int(lm[i * 2 + 1])), 2, (0, 0, 255), -1)
    cv2.imshow('out', frame)
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
```

## Additional convenient functions
```python
def detect_face_centerface(image, threshold=0.35):
    """Convenient wrapper of CenterFace face detection.
    For simple installation, follow https://github.com/dhp252/CenterFace
    instruction.
    !NOTICE: This function should not be used in real application or for speed
    benchmark because the `centerface` instance will be initilaize every call.

    Example:
    >>> lena = cv2.imread('...')
    >>> dets, lms = detect_face_centerface(lena)
    """

    try:
        from centerface import CenterFace
    except ImportError:
        raise ImportError('Install https://github.com/dhp252/CenterFace first')\
            from None

    h, w = image.shape[:2]
    centerface = CenterFace(landmarks=True)
    dets, lms = centerface(image, h, w, threshold=threshold)
    return dets, lms


def draw_centerface(img0, dets, lms, put_score=False):
    """Plot result from centerface face detection.

    Example:
    >>> img = cv2.imread('...')
    >>> dets, lms = detect_face_centerface(img)
    >>> result_img = draw_centerface(img, dets, lms, put_score=False)
    >>> cv2.imshow('', result_img)
    """
    img = img0.copy()

    if put_score:
        tl = round(0.001 * (img.shape[0] + img.shape[1]) / 2) + 1
        tf = max(tl - 1, 1)  # font thickness

    for det in dets:
        box, score = det[:4], det[4]
        cv2.rectangle(img, (int(box[0]), int(box[1])),
                      (int(box[2]), int(box[3])), (2, 255, 0), 1)
        if put_score:
            cv2.putText(img, score, (box[0], box[1] - 2), 0, tl / 3,
                [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
    for lm in lms:
        for i in range(0, 5):
            cv2.circle(img, (int(lm[i * 2]), int(lm[i * 2 + 1])),
                       2, (0, 0, 255), -1)
    return img
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
