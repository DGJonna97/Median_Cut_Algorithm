using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.UI;

[RequireComponent(typeof(Camera))]
public class ExposureSettings : MonoBehaviour
{
    public Volume PreviewCameraVolume;
    public Material CustomRenderMat;
    private Camera cam;
    [Range(0, 24)]
    public int ISO;
    [Range(0, 24)]
    public int Shutter_Speed;
    [Range(0, 18)]
    public float Aperture;
    [Range(0, 1)]
    public float ISO_M;
    [Range(0, 1)]
    public float Shutter_Speed_M;
    [Range(0, 1)]
    public float Aperture_M;
    [Range(1, 300)]
    public float Focal_Length;
    [Range(1, 4)]
    public int Mode;
    public Slider aperture_slider;
    public Slider iso_slider;
    public Slider shutterSpeed_slider;

    private LiftGammaGain _LiftGammaGain;
    private FilmGrain _FilmGrain;
    private kTools.Motion.MotionBlur _MotionBlur;
    private DepthOfField _DOF;
    private float lgg_aperture;
    private float lgg_shutter_speed;
    private float lgg_ISO;
    private float sse;
    // Start is called before the first frame update
    void Start()
    {
        Mode = 1;
        Aperture = 16;
        Focal_Length = 25;
        Shutter_Speed_M = 0.1f;
        Aperture_M = 0.1f;
        ISO_M = 0.1f;
        PreviewCameraVolume.profile.TryGet<LiftGammaGain>(out _LiftGammaGain);
        PreviewCameraVolume.profile.TryGet<FilmGrain>(out _FilmGrain);
        PreviewCameraVolume.profile.TryGet<kTools.Motion.MotionBlur>(out _MotionBlur);
        PreviewCameraVolume.profile.TryGet<DepthOfField>(out _DOF);
        cam = GetComponent<Camera>();
        _DOF.focusDistance.value = 3f;
        _LiftGammaGain.lift.value = new Vector4(0, 0, 0, 0);
        _LiftGammaGain.gamma.value = new Vector4(0, 0, 0, 0);
        _LiftGammaGain.gain.value = new Vector4(0, 0, 0, 0);
        iso_slider.value = 11;
        aperture_slider.value = 9;
        shutterSpeed_slider.value = 11;
    }

    // Update is called once per frame
    void Update()
    {
        Aperture = aperture_slider.value;
        Shutter_Speed = (int)shutterSpeed_slider.value;
        ISO = (int)iso_slider.value;

        SetExposureSettings();
    }

    private void SetExposureSettings()
    {
        ApplyApertureEffects();
        ApplyShutterSpeedEffects();
        ApplyISOEffects();
        ApplyLiftGammaGain();
    }

    private void ApplyApertureEffects()
    {
        //TODO: Apply DOF effect
        //Depth of field seems to be focusing a bit more on the focal length value.
        float focal_val = Remap(Aperture, 1, 32, 1, 300);
        float aperture_inv = (Aperture * -1) + 33;
        _DOF.focalLength.value = focal_val * -1 + 301;
        _DOF.aperture.value = aperture_inv;
        cam.focalLength = Focal_Length;

    }

    private void ApplyShutterSpeedEffects()
    {
        sse = Remap(Shutter_Speed, 0, 24, -10, 10);
        //Currently just sets values to 0, making no change to the shot
        _MotionBlur.intensity.value = -0.05f * (Shutter_Speed - 10); //TODO: adjust motionblur on postproccesing effect AND the custom render texture material
        CustomRenderMat.SetFloat("_Blend", Mathf.Clamp(-0.05f * (sse - 10), 0.1f, 0.9f));
    }

    private void ApplyISOEffects()
    {
        //Adds noise to the image
        _FilmGrain.intensity.value = 0.1f * ISO;
    }

    private void ApplyLiftGammaGain()
    {
        lgg_aperture = Remap(Aperture, 0, 18, -10, 10);
        lgg_shutter_speed = Remap(Shutter_Speed, 0, 24, -10, 10);
        lgg_ISO = Remap(ISO, 0, 24, -10, 10);
        Vector4 NewLift = new Vector4(
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1));

        Vector4 NewGamma = new Vector4(
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1));
        /*
         Vector4 NewGain = new Vector4(
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1),
            Mathf.Clamp((-Aperture_M * lgg_aperture + -Shutter_Speed_M * lgg_shutter_speed + ISO_M * lgg_ISO) / 3, -1, 1));
        */

        _LiftGammaGain.lift.value = NewLift;
        _LiftGammaGain.gamma.value = NewGamma;
        //_LiftGammaGain.gain.value = NewGain;
    }

    /*
    Function to remap values from one range to another.
    variables (value to remap, range from min, range from max, range to min, range to max)
    */
    private float Remap(float value, int fromMin, int fromMax, int toMin, int toMax)
    {
        float normalizedValue = Mathf.InverseLerp(fromMin, fromMax, value);
        float newVal = Mathf.Lerp(toMin, toMax, normalizedValue);
        return newVal;
    }
}
