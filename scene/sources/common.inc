background { color Black }

camera {
  location <0, -20, 0>
  look_at <0, 0, 0>
  right x
  up z
  sky <0,0,1>
  angle 7.7
}

// Sun
light_source { <5, -5, 10> color White }

// Ground reflections
light_source {
  <0, -5, -20>
  color rgb <0.2, 0.2, 0.2>
}