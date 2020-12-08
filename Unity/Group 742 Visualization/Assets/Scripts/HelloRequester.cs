using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;
using System.Collections.Generic;
using System.Linq;
using System;
using System.IO;
/// <summary>
///     Example of requester who only sends Hello. Very nice guy.
///     You can copy this class and modify Run() to suits your needs.
///     To use this class, you just instantiate, call Start() when you want to start and Stop() when you want to stop.
/// </summary>
/// 
namespace SimpleJSON
{
    public class HelloRequester : RunAbleThread
    {
        public Sprite finalsprite;
        private int m;
        private int nl;
        private int cim;
        public ImageHolderScipt test;

        public HelloRequester(int method, int nLig, int cImg, ImageHolderScipt img)
        {
            this.m = method;
            this.nl = nLig;
            this.cim = cImg;
            test = img;

        }

        /// <summary>
        ///     Request Hello message to server and receive message back. Do it 10 times.
        ///     Stop requesting when Running=false.
        /// </summary>
        protected override void Run()
        {
            ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet
            using (RequestSocket client = new RequestSocket())
            {
                client.Connect("tcp://localhost:5555");

                for (int i = 0; i < 1 && Running; i++)
                {
                    //  Debug.Log("Sending Image");
                    
                    client.SendFrame(m + "," + nl + "," + cim);
                    // ReceiveFrameString() blocks the thread until you receive the string, but TryReceiveFrameString()
                    // do not block the thread, you can try commenting one and see what the other does, try to reason why
                    // unity freezes when you use ReceiveFrameString() and play and stop the scene without running the server
                    //                string message = client.ReceiveFrameString();
                    //                Debug.Log("Received: " + message);
                    string message = null;
                    bool gotMessage = false;
                    while (Running)
                    {
                        gotMessage = client.TryReceiveFrameString(out message); // this returns true if it's successful
                        if (gotMessage) break;
                    }

                    if (gotMessage)
                    {

                        test.bytes = message;
                        test.didithappen = true;
                      

                        //byte[] imageBytes = Convert.FromBase64String(message);
                        //File.WriteAllBytes("test.png", message);
                        /*Texture2D tex = new Texture2D(100, 100);
                        tex.LoadImage(message);
                        Sprite sprite = Sprite.Create(tex, new Rect(0.0f, 0.0f, tex.width, tex.height), new Vector2(0.5f, 0.5f), 100.0f);
                        finalsprite = sprite;
                        Debug.Log(finalsprite.name);*/
                        //List<string> results = new List<string>();
                        //var output = message.Split('(', ')').Where((item, index) => index % 2 != 0).ToList();
                        //foreach (var reg in output)
                        //{
                        //Debug.Log(reg);


                        //}
                    }
                }
            }

            NetMQConfig.Cleanup(); // this line is needed to prevent unity freeze after one use, not sure why yet
        }
    }
}