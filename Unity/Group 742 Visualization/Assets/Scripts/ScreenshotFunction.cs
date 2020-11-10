using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScreenshotFunction : MonoBehaviour
{
    public string screenshotName = "test";
    public HelloRequester _helloRequester;
    
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Texture2D testImage = ScreenCapture.CaptureScreenshotAsTexture();
            // Debug.Log("Sending " + imageobject.name + " to python");

            // Texture2D rawImageTexture = (Texture2D)imageobject.sprite.texture;
            byte[] jpegData = testImage.EncodeToJPG();
            //Debug.Log(jpegData.ToString());

            _helloRequester = new HelloRequester(jpegData);
            _helloRequester.Start();
        }
    }
}
