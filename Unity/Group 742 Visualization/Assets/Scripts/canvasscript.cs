using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class canvasscript : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject imageholder;
    public GameObject button;
    public Toggle vizlig;
    public FirstPersonLook fpl;
    public FirstPersonMovement fpm;
    public GameObject lightdad;

    public int m; // 0 = median, 1 = kmeans, 2 = deep
    public int nLig; // 0 = choose, 1 = 16, 2  = 32...
    public int cImg; // 0 = left, 1 = right
    bool ison = false;


    void Start()
    {
        vizlig.onValueChanged.AddListener(delegate {
            ToggleValueChanged(vizlig);
        });
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
   
                enable();
         
        }
        if (Input.GetKeyDown(KeyCode.LeftShift))
        {
            StartCoroutine(CaptureScreen());
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            disable();
        }
    }

    void ToggleValueChanged(Toggle change)
    {
        if (vizlig.isOn)
        {
            foreach (Transform light in lightdad.transform)
            {
                light.GetChild(0).gameObject.SetActive(true);
            }
        }
        else
        {
            foreach (Transform light in lightdad.transform)
            {
                light.GetChild(0).gameObject.SetActive(false);
            }
        }
    }

    void enable()
    {
        imageholder.SetActive(true);
        button.SetActive(false);
        fpl.enabled = false;
        fpm.enabled = false;
    }

    public void disable()
    {
        imageholder.SetActive(false);
        button.SetActive(true);
        fpl.enabled = true;
        fpm.enabled = true;
    }

    public IEnumerator CaptureScreen()
    {
        yield return null;

        string method ="";
        switch (m)
        {
            case 0:
                method = "mediancut";
                break;
            case 1:
                method = "kmeans";
                break;
            case 2:
                method = "cnn";
                break;
            default:
                method = "nonsense";
                break;
        }

        string whichpic = "";
        if (cImg == 0)
        {
            whichpic = "left";
        }
        else
        {
            whichpic = "right";
        }

        this.gameObject.GetComponent<Canvas>().enabled = false;
        yield return new WaitForEndOfFrame();
        ScreenCapture.CaptureScreenshot(Application.dataPath + "/screenshots/" + whichpic+  method + (Mathf.Pow(2,3+nLig)).ToString() + ".png");
        this.gameObject.GetComponent<Canvas>().enabled = true;
        UnityEditor.AssetDatabase.Refresh();
        //Debug.Log(jpegData.ToString());

        //_helloRequester = new HelloRequester(jpegData, test);
        //_helloRequester.Start();
    }
}
