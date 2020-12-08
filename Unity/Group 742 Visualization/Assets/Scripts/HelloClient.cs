using UnityEngine;
using System;
using System.Text;
using UnityEngine.UI;

namespace SimpleJSON
{
    public class HelloClient : MonoBehaviour
    {
        public HelloRequester _helloRequester;
        public Sprite hej;
        private void Start()
        {

            // Sprite img = GameObject.Find("image").GetComponent<Image>().sprite;

            //  Texture2D rawImageTexture = (Texture2D)hej.texture;
            // byte[] jpegData = rawImageTexture.EncodeToJPG();
            // Debug.Log(jpegData.ToString());
            // string str = Encoding.Default.GetString(jpegData);

            //  _helloRequester = new HelloRequester(jpegData);
            //  _helloRequester.Start();
        }

        private void OnDestroy()
        {
            //_helloRequester.Stop();
        }
    }
}