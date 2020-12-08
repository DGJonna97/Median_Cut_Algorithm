using System.Collections;
using System.Collections.Generic;
using UnityEngine;


namespace SimpleJSON
{
    public class ScreenshotFunction : MonoBehaviour
    {
        public string screenshotName = "test";
        public HelloRequester _helloRequester;
        public ImageHolderScipt test;
        public GameObject canvas;

        private void Start()
        {

        }

        // Update is called once per frame
        void Update()
        {
            if (Input.GetKeyDown(KeyCode.Space))
            {
                StartCoroutine(CaptureScreen());
            }
        }

        public IEnumerator CaptureScreen()
        {
            yield return null;
            canvas.SetActive(false);
            yield return new WaitForEndOfFrame();
            Texture2D testImage = ScreenCapture.CaptureScreenshotAsTexture();
            canvas.SetActive(true);

            // Debug.Log("Sending " + imageobject.name + " to python");

            // Texture2D rawImageTexture = (Texture2D)imageobject.sprite.texture;
            byte[] jpegData = testImage.EncodeToJPG();
            //Debug.Log(jpegData.ToString());

            //_helloRequester = new HelloRequester(jpegData, test);
            //_helloRequester.Start();
        }
    }
}