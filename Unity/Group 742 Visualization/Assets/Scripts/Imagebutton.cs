using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Imagebutton : MonoBehaviour
{
    // Start is called before the first frame update
    public Image imageobject;
    public Sprite img;
    void Start()
    {
        img = GetComponent<Image>().sprite;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void onclick()
    {
        imageobject.sprite = img;
        imageobject.gameObject.SetActive(true);
    }

    public void setimage(Sprite inputimg)
    {
        img = inputimg;
    }
}
