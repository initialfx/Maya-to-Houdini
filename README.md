## What?
한국어로 서비스할 예정입니다. 몇가지 수정사항에 대해서 공지하도록 할께요.
## Why?

At the moment is FBX the standard format to transfer scenes between different software. The problem is that FBX does not recognize a plugin data and just throws it away.
It is handy to have exactly the same light-setup in both the software-packages.
Otherwise the simulation's will not align  when brought together.

FBX로 데이타를 마야에서 후디니로 보내는거 보다는 일단 데이타를 모두 읽어서 JSON타입의 데이타셋으로 저장한 다음 후디니에서 다시 불러와서 라이트 리그를 재구성합니다. 어렵지 않고 그냥 직관적입니다. 
## How?

Inside Maya, copy the content of the script in the 'Script Editor'. Click 'Add to shelf' to keep it when restarting.
Run the script and select all the lights you want to export. **Redshift-lights only**

Click the upper button. The script wil detect if selected lights are parented to controllers. 
It will duplicate them outside of the parent and bakes it into the world.

Select the baked **duplicate** lights and any other light that had no parent.
Click the lower button and choose a path to export the .json file with all the light-attributes inside.

Open Houdini > source editor and run  **houdini_transformer.py**
Select the .json and see the magic! 

![0ff36ec841eb3d64d4298753de060f3f](https://user-images.githubusercontent.com/44348300/47940627-8bdd0a00-deeb-11e8-89af-e0f9c20ff044.png)


### what does not work?

It only works for physical based lights (you should use them 99% of the time eitherway).

In earlier versions of Redshift there is a bug, take the latest and greatest.

Path select with ``$HIP/Desktop/`` in Houdini does not work.

Just insert ``C:/Users/Desktop/`` as path.

