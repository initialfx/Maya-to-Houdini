import json

def filePath():
    """ ask for file path"""
    filepath = hou.ui.selectFile()
    return filepath

def getData(filename):
    return eval(open(filename).read(), {"false": False, "true":True})

temp_data = getData(filePath())

for i in range(len(temp_data)):
    #print(dict[i])
    
    data = temp_data[i]
    
    # Create Root Null
    sceneroot = hou.node('/obj')
    globalnull = sceneroot.createNode('null', 'size_locator')
    globalnull.setParms({'scale': 1})
    
    
    # Create RS_Light
    light = hou.node("/obj").createNode('rslight', 'Key')
    
    light.setInput(0, globalnull)
    hou.node("obj").layoutChildren()
    
    light.parmTuple('t').set(tuple(data["translate"][0]))
    light.parmTuple('r').set(tuple(data["rotate"][0]))
    
    light.parm('RSL_intensityMultiplier').set(data["intensity"])    
    light.parm('Light1_exposure').set(data["exposure"])
    
    light.parm('RSL_affectDiffuse').set(data["affectsDiffuse"])
    light.parm('RSL_bidirectional').set(data["areaBidirectional"])
    light.parm('RSL_visible').set(data["areaVisibleInRender"])
    light.parm('RSL_volumeScale').set(data["volumeRayContributionScale"])
    light.parm('RSL_areaShape').set(data["areaShape"])
    
    light.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    light.setComment(data["name"])



#attributes = ['scale', 'rotate', 'translate', 'intensity', 'color', 'affectsDiffuse', 'affectsSpecular','areaVisibleInRender', 'areaBidirectional', 'volumeRayContributionScale', 
#    'exposure', 'areaShape','spotConeAngle', 'areaSamples','areaSpread','on', 'colorR', 'colorG','colorB','temperature','colorMode', 'intensity', 
#    'exposure', 'unitsType','lumensperwatt','decayType','falloffStart', 'falloffStop', 'shadow', 'shadowTransparency', 
#    'SAMPLINGOVERRIDES_shadowSamplesScale','SAMPLINGOVERRIDES_numShadowSamples', 'spotConeFalloffAngle',
#    'spotConeFalloffCurve','affectedByRefraction', 'emitGiPhotons', 'emitCausticPhotons','normalize',
#    'photonIntensityMultiplierGI','photonIntensityMultiplierCaustics','diffuseRayContributionScale',
#    'glossyRayContributionScale','singleScatteringRayContributionScale','multipleScatteringRayContributionScale',
#    'indirectRayContributionScale', 'indirectMaxTraceDepth', 'volumeRayContributionScale','volumeNumSamples','dropoff']   

