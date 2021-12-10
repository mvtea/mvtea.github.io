---
permalink: /research/
title: "Research"
excerpt: "About me"
author_profile: true
redirect_from: 
---

Here, you'll find a (hopefully) accessible background and a summary of my work on my major research projects. 

<center>
  <h2>Current Projects</h2>
</center>

### Characterizing black hole X-ray binaries (BHXRBs) with _Chandra_

Stellar-mass black holes are most often observed via interaction with a companion star, which orbit one another in what's known as an [X-ray binary](https://en.wikipedia.org/wiki/X-ray_binary) (XRB). These systems earn their name from the high-energy emission generated when the black hole accretes material from its companion, observed here on Earth as X-rays by space-based observatories like [_Chandra_](https://chandra.harvard.edu/).

All compact objects -- black holes, neutron stars, and white dwarfs -- have the capacity to form X-ray binaries due to their strong gravity. Black hole XRBs in particular are known to cycle through distinct emission states tied directly to their accretion rate. Studying in detail the energy signature and variability of a particular XRB -- _especially_ as the system evolves through multiple emission states -- can reveal much about the nature of the system itself, their gravitational effects on their environment, and the high-energy physics powering their emission.

The detailed analysis required to confidently classify and characterize these systems is prohibitively time-consuming for large samples, but with each newly-examined system comes improved constraints to the BHXRB population's parameter space, making them easier to identify and study. As part of my 2021 honors thesis in the Wesleyan University astronomy department, advised by [Prof. Roy Kilgard], I performed such an analysis for the ~80 brightest (in flux) extragalactic X-ray sources outside of the Local Group. The initial sample comes from the Kilgard group's database of 45,000+ observations of such sources from the _Chandra_ archive. 

My thesis work itself identified 11 candidate XRBs, the majority of which have not been studied in detail in the literature, and many of which are candidate XRBs. (This work is under embargo until June 2022.) In a forthcoming paper, myself and Dr. Kilgard will utilize these results to suggest a new photometric method for identifying and classifying ultraluminous X-ray binaries with _Chandra_; I also intend to make the Python tools I developed for this work open-source. I presented this work as a [poster]() at the AAS 237 in January of 2021.

| ![BHB](https://images.ctfassets.net/cnu0m8re1exe/5BIngirakRnX3gIKHE3c2M/63905ab53aa5b2b8cf3f1fa5b4013f94/bhbinary_xmm_960.jpg?w=650&h=433&fit=fill) | 
|:--:| 
| *An artist's rendition of the HMXB Cyg-X1, one of the first discovered and most well-studied XRBs. (Credit: NASA, CXC, M. Weiss)* |

<br/><br/>

<center>
  <h2>Previous Projects</h2>
</center>

### Simulating the Solar Gravitational Lens (SGL)

Light tends to take the shortest path as it travels through the universe. When it encounters a massive object (e.g. a galaxy,or a cluster of galaxies), the shortest path becomes a _curved_ path, as spacetime is warped in the presence of matter. This means that, from here on Earth, we sometimes observe the light from objects _behind_ other massive objects like galaxies, as the path of the light is curved around the outside of the object by gravity. This phenomenon is known as [gravitational lensing](https://en.wikipedia.org/wiki/Gravitational_lens).

As the name suggests, astronomers often take advantage of this phenomenon, using massive objects as "lenses" to enhance the data that we get from these objects, much like a telescope lens. While galaxies and clusters boast the most mass and are usually used for these kinds of studies, any massive object can act as a lens in this way, including stars like our own Sun. If we were to place a telescope at about 550 au from the Sun and align it perfectly with a target -- say, an exoplanet -- we would see the light from the planet immensely magnified and spread out in a ring around the outside of the Sun. This _Einstein ring_ would contain a high-resolution image of the surface of the exoplanet, equivalent to a modern sattelite image of the state of Connecticut. Such a telescope is in the planning stage, and is known as the [Solar Gravitational Lens](https://en.wikipedia.org/wiki/Solar_gravitational_lens) (SGL).

Problem is, the image is warped into this ring and needs to be reconstructed, which is easier said than done. My early undergraduate work, advised by [Prof. Seth Redfield](https://sethredfield.wescreates.wesleyan.edu/), focused on this problem. Toward this end, I developed [SunTracer](https://github.com/mvtea/sgl), a relativistic raytracer which simulates images as they would be seen by the SGL. This was the first step toward a deconvolution method for the aforementioned problem, meant to generate a training set for a machine-learning algorithm which would reproduce the original exoplanet images.

I chose to transition to a new project after developing SunTracer, and the deconvolutional methods for these images are being worked on by other, more qualified parties, namely Dr. Slava Turyshev and Dr. Victor T. Toth at JPL; interested parties may read the SGL group's [NIAC Final Report](https://arxiv.org/pdf/2002.11871.pdf) (for which they [recently recieved Phase III funding](https://www.nasa.gov/press-release/nasa-selects-early-stage-technology-concepts-for-new-continued-study). Or, for a lighter read, [my paper](https://mvtea.github.io/files/tea_knac2019.pdf) from my talk on the subject at KNAC in fall of 2019.

| ![erf.png](https://mvtea.github.io/files/erf.png) | 
|:--:| 
| *Images of a habitable planet as seen by the SGL.* Here, I utilized RGB data from NASA’s EPIC camera aboard the DSCOVR satellite as the source for SunTracer, which warped the image into an Einstein ring. (*M. V. Tea*)|
