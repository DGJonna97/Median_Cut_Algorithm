using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.Scripting.Python;
using UnityEditor;
using System.IO;

//It does not work yet, but it will allow us to run the Python code in Unity.
public class medianCutAlgorithm
{
    [MenuItem("Python/medianCutAlgorithm")]
    static void RunscriptName()
        {
            string scriptPath = Path.Combine(Application.dataPath, "file name");
            PythonRunner.RunFile(scriptPath);
        }
}
