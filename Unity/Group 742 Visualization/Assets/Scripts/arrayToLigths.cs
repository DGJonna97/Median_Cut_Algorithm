using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

[Serializable]
public class arrayToLigths : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject prefablight;
    public Cubemap cm;
    public Texture2D church;
    int h = 1000, w = 1000;
    public int r = 50;
    public string regions;
    public GameObject lightdad;
    /*public int[,] tempresults = new int[,] {
        { 35, 53  },
        { 119, 53 },
        { 215, 53 },
        { 312, 53 },
        {  71, 159 },
        { 71, 293 },
        { 252, 165 },
        { 252, 299 },
        { 425, 90 },
        { 529, 90 },
        { 428, 278  },
        { 532, 278 },
        { 626, 59 },
        { 716, 59 },
        { 660, 184 },
        { 660, 312 },
    };*/

    public int[,] tempresults = new int[,] {
        { 565, 291  },
        { 165, 245 },
        { 451, 50 },
        { 57, 77 },
        {  322, 63 },
        { 699, 67 },
        { 301, 187 },
        { 438, 289 },
        { 584, 145 },
        { 510, 178 },
        { 69, 311  },
        { 82, 194 },
        { 192, 78 },
        { 688, 274 },
        { 587, 49 },
        { 274, 324 },
    };

    void Start()
    {
        
    }

    Vector2 toPolar(Vector2 xy, int RadialScale, int LengthScale)
    {
        
        float radius =  2.0f * 2.0f * RadialScale;
        float angle = Mathf.Atan2(xy.x, xy.y) * 1.0f / 6.28f * LengthScale;
        Vector2 oout = new Vector2(radius, angle);
        return oout;
    }


    // Update is called once per frame
    public float distance = 50f;
    //replace Update method in your class with this one
    void FixedUpdate()
    {
        //if mouse button (left hand side) pressed instantiate a raycast
        if (Input.GetMouseButtonDown(0))
        {
            //create a ray cast and set it to the mouses cursor position in game
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit, distance))
            {
                //draw invisible ray cast/vector
                Debug.DrawLine(ray.origin, hit.point);
                //log hit area to the console
                

            }
        }
    }

    public void genligths(List<int> centerxints, List<int> centeryints, List<int> redints, List<int> greenints, List<int> blueints)
    {
        for (int i = 0; i < lightdad.transform.childCount; i++)
        {
            Transform c = lightdad.transform.GetChild(i);
            Destroy(c.gameObject);
        }

        
        for (int i = 0; i < centerxints.Count; i++)
        {
            Vector2 ost = new Vector2(centerxints[i], centeryints[i]);
            
            //Debug.Log(i);

            float inputx = (float)ost.x;
            float inputy = (float)ost.y;

            float azim = Mathf.Atan2( inputy, inputx) * Mathf.Rad2Deg;
            float polar = Mathf.Atan(inputy /inputx) * Mathf.Rad2Deg;
     
            float x = r * Mathf.Sin(polar) * Mathf.Cos(azim);
            float y = r * Mathf.Sin(polar) * Mathf.Sin(azim);
            float z = r * Mathf.Cos(polar);
            
            Color c = new Color((float)redints[i] / 255f, (float)greenints[i] / 255f, (float)blueints[i] / 255f);
            GameObject lights = Instantiate(prefablight, new Vector3(x,y,z), Quaternion.identity, lightdad.transform);
            lights.GetComponent<Light>().color = c;

//Vector2 post = sphere_coords(xycoordinates[i, 0], xycoordinates[i, 1]);
//Vector3 post2 = new Vector3(post.x,0,post.y);
        }


    }
    Vector3 sphere_coords(int x,int y)
    {
        float theta = 2 * (float)x / (float)w - 1;
        float phi = 2 * (float)y / (float)h - 1;
        //Vector2 pos = new Vector2((phi * (Mathf.PI / 2)), theta * Mathf.PI);
        float x2 = Mathf.Cos(phi) * Mathf.Cos(theta);
        float y2 = Mathf.Sin(phi);
        float z2 = Mathf.Cos(phi) * Mathf.Sin(theta);
        return new Vector3(z2,x2,y2)*10;
    }


    Color lightColors(float x, float y)
    {
        // Texture2D ost = (Texture2D)church.mainTexture;
           return church.GetPixel((int)x,(int) y);
    }

}
