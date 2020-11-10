using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class ImageHolderScipt : MonoBehaviour
{

    public Sprite[] images;
    
    public int index = 0;
    public Image imageobject;
    public Button left;
    public Button right;
    public Button analyse;
    public HelloRequester _helloRequester;
    // Start is called before the first frame update
    void Start()
    {
       // imageobject = transform.GetChild(0).GetComponent<Image>().sprite;


    }

    // Update is called once per frame
    void Update()
    {
        imageobject.sprite = images[index];
        //Debug.Log(imageobject.name);

        if (index == 0)
        {
            left.gameObject.SetActive(false);
        }
        else
        {
            left.gameObject.SetActive(true);
        }

        if (index == images.Length-1)
        {
            right.gameObject.SetActive(false);
        }
        else
        {
            right.gameObject.SetActive(true);
        }
    }

    public void leftbuttonclick()
    {
        index--;
    }

    public void rightbuttonclick()
    {
        index++;
    }

    public void analysebuttonclick()
    {
        Debug.Log("Sending " + imageobject.name + " to python");

        Texture2D rawImageTexture = (Texture2D)imageobject.sprite.texture;
        byte[] jpegData = rawImageTexture.EncodeToJPG();
        //Debug.Log(jpegData.ToString());

        _helloRequester = new HelloRequester(jpegData);
        _helloRequester.Start();
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}
