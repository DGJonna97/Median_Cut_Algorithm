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
    public Texture2D left;
    public Texture2D right;
    public Texture2D church;
    int h = 1000, w = 1000;
    public int r = 50;
    public string regions;
    public GameObject lightdad;
    Vector3 target;
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
        target = new Vector3(0, 0, 0);
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

    public static double MapCoordinate(double i1, double i2, double w1,
    double w2, double p)
    {
        return ((p - i1) / (i2 - i1)) * (w2 - w1) + w1;
    }

    public void genligths(List<int> centerxints, List<int> centeryints, List<int> redints, List<int> greenints, List<int> blueints, Material pic)
    {
       // r = centerxints.Count;
        Texture2D normalizer;
        if (pic.name== "New Material 1")
        {
            normalizer = left;
        }
        else
        {
            normalizer = right;
        }

        int w = normalizer.width;
        int h = normalizer.height;

        for (int i = 0; i < lightdad.transform.childCount; i++)
        {
            Transform c = lightdad.transform.GetChild(i);
            Destroy(c.gameObject);
        }
        double phi0 = 0.0;
        double phi1 = Math.PI;
        double theta0 = 0.0;
        double theta1 = 2.0 * Math.PI;

       

        for (int i = 0; i < centerxints.Count; i++)
        {
            Vector2 ost = new Vector2(centerxints[i], centeryints[i]);
            double theta = MapCoordinate(0.0, w - 1,
              theta1, theta0,ost.x);
            double phi = MapCoordinate(0.0, h - 1, phi0,
                phi1,ost.y);
            // find the cartesian coordinates
            double x = r * Math.Sin(phi) * Math.Cos(theta);
            double y = r * Math.Sin(phi) * Math.Sin(theta);
            double z = r * Math.Cos(phi);

            GameObject lights = Instantiate(prefablight, new Vector3((float)x, (float)z,(float)y), Quaternion.identity, lightdad.transform);

           // Color c = new Color((float)redints[i] / 255f, (float)greenints[i] / 255f, (float)blueints[i] / 255f);
            Light l = lights.GetComponent<Light>();
            //l.color = c;
            l.intensity = intensityofpoint(ost.x, ost.y, normalizer)/((float)centerxints.Count/5f);


            lights.transform.LookAt(target);
            /*Vector2 ost = new Vector2(centerxints[i], centeryints[i]);
            float r2 = r / h;

            float longitude = ost.x / w;

            float latitude = 2f * Mathf.Atan((float)Math.Exp(ost.y / r2)) - Mathf.PI / 2f;

            Vector3 p = new Vector3(
               r * Mathf.Cos(latitude) * Mathf.Cos(longitude),
               r * Mathf.Cos(latitude) * Mathf.Sin(longitude),
               r * Mathf.Sin(latitude));

            GameObject lights = Instantiate(prefablight, p, Quaternion.identity, lightdad.transform);
           

            Vector2 ost = new Vector2(centerxints[i], centeryints[i]);

             //Debug.Log(i);

             float inputx = (float)ost.x/w; //needs to be normalized
             float inputy = (float)ost.y/h;

             float azim = Mathf.Atan2( inputx, inputy);
             float polar = Mathf.Atan(inputx /inputy);

             float x = r * Mathf.Cos(polar) * Mathf.Cos(azim);
             float y = r * Mathf.Cos(polar) * Mathf.Sin(azim);
             float z = r * Mathf.Sin(polar);

            
             //point them to 0,0  offset by -5 to 0.5

             //Vector2 post = sphere_coords(xycoordinates[i, 0], xycoordinates[i, 1]);
             //Vector3 post2 = new Vector3(post.x,0,post.y); */
        }


    }
    float intensityofpoint(float x, float y, Texture2D image)
    {
        Color c = image.GetPixel((int)x, (int)y);
        c.r = 0.2125f * c.r;
        c.g = 0.7154f * c.g;
        c.b = 0.0721f * c.b;
        float intensity = c.r + c.g + c.b;
        return intensity;
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
