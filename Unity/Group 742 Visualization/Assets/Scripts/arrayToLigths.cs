using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class arrayToLigths : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject prefablight;
    public Cubemap cm;
    int h = 1000, w = 1000;
    int r = 50;
    public int[,] tempresults = new int[,] {
        { 162, 82  },
        { 162, 283 },
        { 385, 132 },
        { 385, 333 },
        {  92, 545 },
        { 281, 545 },
        { 412, 464 },
        { 412, 608 },
        { 486, 162 },
        { 486, 388 },
        { 719, 89  },
        { 719, 314 },
        { 480, 486 },
        { 480, 605 },
        { 586, 569 },
        { 785, 569 },
    };

    void Start()
    {
        genligths(tempresults);
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
                Debug.Log(hit.point);

            }
        }
    }

    void genligths(int[,] xycoordinates)
    {
        for (int i = 0; i < xycoordinates.Length/2; i++)
        {
            Vector2 ost = new Vector2(xycoordinates[i, 0], xycoordinates[i, 1]);
            Debug.Log(ost);
            float inputx = xycoordinates[i, 0];
            float inputy = xycoordinates[i, 1];

            float azim = Mathf.Atan2( inputy, inputx) * Mathf.Rad2Deg;
            float polar = Mathf.Atan(inputy /inputx) * Mathf.Rad2Deg;
     
            float x = r * Mathf.Sin(polar) * Mathf.Cos(azim);
            float y = r * Mathf.Sin(polar) * Mathf.Sin(azim);
            float z = r * Mathf.Cos(polar);
            
            Instantiate(prefablight, new Vector3(x,y,z), Quaternion.identity);

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


    Vector3 UvTo3D(Vector2 uv)
    {
        Mesh mesh = GetComponent<MeshFilter>().mesh;
        int[] tris = mesh.triangles;
        Vector2[] uvs = mesh.uv;
        Vector3[] verts = mesh.vertices;
        for (int i = 0; i < tris.Length; i += 3)
        {
            Vector2 u1 = uvs[tris[i]]; // get the triangle UVs
            Vector2 u2 = uvs[tris[i + 1]];
            Vector2 u3 = uvs[tris[i + 2]];
            // calculate triangle area - if zero, skip it
            float a = Area(u1, u2, u3); if (a == 0) continue;
            // calculate barycentric coordinates of u1, u2 and u3
            // if anyone is negative, point is outside the triangle: skip it
            float a1 = Area(u2, u3, uv) / a; if (a1 < 0) continue;
            float a2 = Area(u3, u1, uv) / a; if (a2 < 0) continue;
            float a3 = Area(u1, u2, uv) / a; if (a3 < 0) continue;
            // point inside the triangle - find mesh position by interpolation...
            Vector3 p3D = a1 * verts[tris[i]] + a2 * verts[tris[i + 1]] + a3 * verts[tris[i + 2]];
            // and return it in world coordinates:
            return transform.TransformPoint(p3D);
        }
        // point outside any uv triangle: return Vector3.zero
        return Vector3.zero;
    }

    float Area(Vector2 p1, Vector2 p2, Vector2 p3)
    {
        Vector2 v1 = p1 - p3;
        Vector2 v2 = p2 - p3;
        return (v1.x * v2.y - v1.y * v2.x) / 2;
    }

}
