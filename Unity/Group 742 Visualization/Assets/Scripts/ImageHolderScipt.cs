using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class ImageHolderScipt : MonoBehaviour
{

    public Sprite[] images;
   
    public Image imageobject;
    public GameObject prefabbutton;
    public GameObject panel;
    public Button analyse;
    public HelloRequester _helloRequester;
    // Start is called before the first frame update
    void Start()
    {
        // imageobject = transform.GetChild(0).GetComponent<Image>().sprite;
       // maxsize = images.Length;
        initializeUI();

    }

    // Update is called once per frame
    void Update()
    {
        

    }

    public void leftbuttonclick()
    {
      //  currentmax -= maxsize;
       // currentmin -= maxsize;
        initializeUI();
    }

    public void rightbuttonclick()
    {
      //  currentmax += maxsize;
       // currentmin += maxsize;
        initializeUI();
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

    public void initializeUI()
    {
      
       /*if (currentmax < maxsize)
        {
            right.gameObject.SetActive(true);
        }
        else
        {
            right.gameObject.SetActive(false);
        }

        if (currentmax > maxsize) 
        {
            left.gameObject.SetActive(true);
        }
        else
        {
            left.gameObject.SetActive(false);
        }*/

       
        

        Vector3 pos = new Vector2(800, 275);
        for (int i = 0; i < images.Length; i++)
        {
            Sprite img = images[i];
            GameObject b = Instantiate(prefabbutton, pos, Quaternion.identity, panel.transform);
            b.GetComponent<Imagebutton>().imageobject = imageobject;
            b.GetComponent<Image>().sprite = img;
            pos.x += 100;
        }  
    }
}
