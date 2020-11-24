using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.Rendering;
using UnityEngine.UI;

public class skyboxbuttons : MonoBehaviour
{
    Image img;
    
    // Start is called before the first frame update
    void Start()
    {
        img = GetComponent<Image>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void click()
    {


        Texture2D selected = img.mainTexture as Texture2D;

        Material material = new Material(Shader.Find("Skybox/Panoramic"));
        material.mainTexture = (Texture)selected;

        RenderSettings.skybox = material;
        DynamicGI.UpdateEnvironment();
    }
}
