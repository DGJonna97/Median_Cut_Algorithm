using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using UnityEngine;
using System.Linq;

namespace SimpleJSON
{


    [System.Serializable]
    public class arrtol2
    {
        // Start is called before the first frame update

        public string message;
        //public string regions;
        public arrayToLigths arr;
        public Material cm;

        public void go(arrayToLigths arr)
        {


            message= message.Replace(@"\", "");
            message = message.Replace("[", "");
            message = message.Replace("]", "");
            message = message.Replace(":", "");
            message = message.Replace("{", "");





            string input = message;
            string pat = "centerx";
            int begining = input.IndexOf(pat) + pat.Length+1;
            int end = input.IndexOf("centery", begining)-3;
            string centersx = input.Substring(begining, end - begining);


            //input.Remove(begining, end);

            string pat2 = "centery";
            int begining2 = input.IndexOf(pat2) + pat2.Length+1;
            int end2 = input.IndexOf("r", begining2)-3;
            string centersy = input.Substring(begining2, end2 - begining2);

            //input.Replace(centersy, "");


            string pat3 ="red";
            int begining3 = input.IndexOf(pat3) + pat3.Length+1;
            int end3 = input.IndexOf("green", begining3)-3;
            string r = input.Substring(begining3, end3 - begining3);
            //Debug.Log(r);
            string pat4 = "green";
            int begining4 = input.IndexOf(pat4) + pat4.Length+1;
            int end4 = input.IndexOf("blue", begining4)-3;
            string g = input.Substring(begining4, end4 - begining4);
            //Debug.Log(g);
            string pat5 = "blue";
            int begining5 = input.IndexOf(pat5) + pat5.Length+1;
            int end5 = message.Length-2;
            string b = input.Substring(begining5, end5 - begining5);
            //Debug.Log(b);
            //var root = JSON.Parse(message2);
            //string centersx = root["centerx"];
            
            

           



            List<int> centerxints = centersx.Split(','). Select(int.Parse).ToList();
            List<int> centeryints = centersy.Split(',').Select(int.Parse).ToList();
            /*List<int> redints = r.Split(',').Select(int.Parse).ToList();
            List<int> greenints = g.Split(',').Select(int.Parse).ToList();
            List<int> blueints = b.Split(',').Select(int.Parse).ToList();-*/

            arr.genligths(centerxints, centeryints, null, null, null, cm);
          

        }

        // Update is called once per frame
        void Update()
        {

        }
    }
}