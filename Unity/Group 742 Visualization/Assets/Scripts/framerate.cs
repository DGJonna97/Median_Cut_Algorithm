using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Linq;
public class framerate : MonoBehaviour
{
     int frameCount = 0;
     double dt = 0.0f;
     double fps = 0.0f;
    List<double> fps2 = new List<double>();
    public int avereagefps;
     double updateRate = 8.0f;  // 4 updates per sec.
    public Text counter;
    // Update is called once per frame
    void start()
    {
        counter =  GetComponent<Text>();
    }

    void Update()
    {
        frameCount++;
        dt += Time.deltaTime;
        if (dt > 1.0 / updateRate)
        {
            fps = frameCount / dt;
            if (fps2.Count > 10)
            {
                fps2.RemoveAt(0);
              
            }
          
            fps2.Add(fps);  
            frameCount = 0;
            dt -= 1.0 / updateRate;
        }
        if (fps2.Count > 0)
        {
            avereagefps = (int)fps2.Average();
            counter.text = avereagefps.ToString();
        }
    }
}
