using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Rendering;

namespace SimpleJSON
{
    public class ImageHolderScipt : MonoBehaviour
    {
        public string bytes;
        public bool didithappen = false;
        public List<Sprite> images;
        public Sprite finalsprite;
        public Material left;
        public Material right;
        public Image imageobject;
        public GameObject prefabbutton;
        public GameObject panel;
        public Button analyse;
        public HelloRequester _helloRequester;
        public arrayToLigths arr;
        public canvasscript canscp;
        Vector3 pos;
        public Dropdown method;
        public Dropdown nLigths;
        public Dropdown chosenimage;
        public arrayToLigths arrtoligs;

        // Start is called before the first frame update
        void Start()
        {
            // imageobject = transform.GetChild(0).GetComponent<Image>().sprite;
            // maxsize = images.Length;
            // initializeUI();
            images = new List<Sprite>();
            pos = new Vector2(100, 100);

           
        }

        // Update is called once per frame
        void Update()
        {
            if (didithappen)
            {
                didithappen = false;
                arrtol2 arr = new arrtol2();
                arr.message = bytes;
               

                if (chosenimage.value == 0)
                {
                    arr.cm = left;
                }
                else
                {
                    arr.cm = right;
                }
                 arr.go(arrtoligs);
            }

        }

        public void buildsprite(string message)
        {

            Texture2D Tex2D;
            byte[] FileData;

            if (File.Exists(message))
            {
                Debug.Log(message);
                FileData = File.ReadAllBytes(message);
                Tex2D = new Texture2D(2, 2);           // Create new "empty" texture
                Tex2D.LoadImage(FileData);
                // Texture2D SpriteTexture = new Texture2D(2, 2);
                Sprite NewSprite = Sprite.Create(Tex2D, new Rect(0, 0, Tex2D.width, Tex2D.height), new Vector2(0, 0), 100);
                //imageobject.sprite = NewSprite;
                images.Add(NewSprite);
                GameObject b = Instantiate(prefabbutton, pos, Quaternion.identity, panel.transform);
                b.GetComponent<Imagebutton>().imageobject = imageobject;
                b.GetComponent<Image>().sprite = NewSprite;
                pos.x += 100;
            }
            else
            {
                Debug.Log("failed " + message);
            }
            /* List<string> results = new List<string>();
              var output = message.Split('(', ')').Where((item, index) => index % 2 != 0).ToList();
              Texture2D texture = imageobject.sprite.texture;
              Color pixelColour = new Color(0, 255, 0, 1);
              foreach (var reg in output)
              {
                  var output2 = reg.Split(',').ToList();
                  int xmin = int.Parse(output2[0]);
                  int xmax = int.Parse(output2[1]);
                  int ymin = int.Parse(output2[2]);
                  int ymax = int.Parse(output2[3]);
                  Debug.Log(reg);
                  Debug.Log(reg[0]);

                  for (int i = xmin; i < xmax; i++)
                  {
                      for (int j = ymin; j < ymax; j++)
                      {
                          texture.SetPixel(i, j, pixelColour);
                          Debug.Log(i.ToString()+" "+ j.ToString());

                      }
                  }

              }


              texture.Apply();
              Sprite sprite2 = Sprite.Create(texture, new Rect(0.0f, 0.0f, texture.width, texture.height), new Vector2(0.5f, 0.5f), 100.0f);
              Debug.Log("hej");
              imageobject.sprite = sprite2;
      /*
              // Sprite sprite = Sprite.Create(texture, new Rect(0, 0, w, h), Vector2.zero);





          //  Debug.Log(bytes[4]);
          /* Texture2D tex = new Texture2D(100, 100);
           tex.LoadImage(bytes);
           Sprite sprite = Sprite.Create(tex, new Rect(0.0f, 0.0f, tex.width, tex.height), new Vector2(0.5f, 0.5f), 100.0f);
           finalsprite = sprite;
           Debug.Log(finalsprite.name);*/

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

        /* public void analysebuttonclick()
         {
             Debug.Log("Sending " + imageobject.name + " to python");

             Texture2D rawImageTexture = (Texture2D)imageobject.sprite.texture;
             byte[] jpegData = rawImageTexture.EncodeToJPG();
             //Debug.Log(jpegData.ToString());

             _helloRequester = new HelloRequester(jpegData, tester);
             _helloRequester.Start();
         }*/

        private void OnDestroy()
        {
            //_helloRequester.Stop();
        }

        public void initializeUI()
        {
            int m = method.value; // 0 = median, 1 = kmeans, 2 = deep
            int nLig = nLigths.value; // 0 = choose, 1 = 16, 2  = 32...
            int cImg = chosenimage.value; // 0 = left, 1 = right

            if (nLig == 0) // didnt choose a value in the choose lights dropdown
            {
                return;
            }

            if (cImg == 0)
            {
                // left image becomes skybox
                RenderSettings.skybox = left;
            }
            else
            {
                //right image becomes skybox
                RenderSettings.skybox = right;
            }
            
            DynamicGI.UpdateEnvironment();
            canscp.m = m;
            canscp.nLig = nLig;
            canscp.cImg = cImg;
            

            _helloRequester = new HelloRequester(m,nLig,cImg, this);
            _helloRequester.Start();
            //canscp.disable();
        }
    }
}
