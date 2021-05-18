---
permalink: /research/
title: "Research"
excerpt: "About me"
author_profile: true
redirect_from: 
---


## Black hole X-ray binaries (BHXRBs)

Compact objects (black holes, neutron stars, and white dwarfs) are often found in binary systems with a companion star, slowly accumulating an accretion disk of stellar material which emits high-energy X-ray radiation. Observations of these X-ray binaries (XRBs) in nearby galaxies provide the best opportunity to study compact objects, their gravitational effects on their environment, and the high-energy physics powering their emission. Black hole XRBs (BHXRBs) are known to cycle through discrete emission states, segregated by their spectral shpe and variability and directly linked to their accretion rate, with analogous states existing for neutron star XRBs (NSXRBs).

The detailed analysis required to confidenfly classify and categorize these systems is prohibitively time-consuming for large samples, but with each new parameterized system comes new constraints to the BHXRB population, making them easier to identify. As part of my 2021 honors thesis in the Wesleyan University astronomy department, I performed such analysis for ~50 of the brightest (in flux) X-ray sources in the local universe under [Dr. Roy Kilgard](http://rkilgard.faculty.wesleyan.edu/). These sources come from the Kilgard group's database of ~45,000 X-ray sources within 15 Mpc from archival *Chandra* observations. From this sample, I have (so far) successfully identified 11 candidate XRBs, the majority of which have not been studied in detail in the literature and many of which are candidate BHXRBs. 

In a forthcoming paper, myself and Dr. Kilgard will utilize these results to suggest a new photometric method for identifying and classifying ultraluminous X-ray binaries.

| ![BHB](https://images.ctfassets.net/cnu0m8re1exe/5BIngirakRnX3gIKHE3c2M/63905ab53aa5b2b8cf3f1fa5b4013f94/bhbinary_xmm_960.jpg?w=650&h=433&fit=fill) | 
|:--:| 
| *An artist's rendition of the HMXB Cyg-X1, one of the first discovered and most well-studied XRBs. (Credit: NASA, CXC, M. Weiss)* |

<br/><br/>

## The Solar Gravitational Lens (SGL)

Gravitational lensing is a phenomenon wherein a massive object, like a galaxy or cluster of galaxies, bends the trajectory of light of a bright source located behind it, which we observe on Earth as a warping or duplication of the source image on the sky. If the conditions are just right and the source, lensing object and observer are perfectly aligned (*in syzygy*), what we observe is called an Einstein ring, a circle of light about the limb of the lens containing highly-magnified light from the source. This alignment, however, rarely occurs in nature.

Strong lensing is only seen occuring around very massive bodies from here on Earth, but this is simply due to the fact that the mass of a given gravitational lens is dependent on the distance from its gravitational focus. That is to say, gravitational lensing can occur for any size object, but all low-mass objects (like stars) are too far from the Earth for us to be at their gravitational focus. The Sun, even, has a gravitational focus at a minimum of ~550AU, and it is this fact that the Solar Gravitational Lens (SGL) seeks to take advantage of.

The SGL is a theoretical space telescope comprised of a meter-class telescope outfitted with a coronagraph, pointed at the Sun, and placed at its gravitational focus. When aligned in syzygy with a target exoplanet, the resulting Einstein ring will contain highly-magnified, extreme-resolution data from the surface of the exoplanet. With the optical properties of the SGL, this is essentially equivalent to a sattelite orbiting Earth taking an image of the state of Connecticut.

From the first few weeks of my time as an undergraduate in 2017 to the end of the summer of 2019, I worked with [Professor Seth Redfield](https://sethredfield.wescreates.wesleyan.edu/) on simulating the images we might see from the SGL once it is positioned, so that we may begin work on a reconstruction algorithm for converting the warped light from the Einstein rings that it gathers back into an image of the source's surface. This project culminated in a general-relativistic raytracing algorithm I call [<b style='font: courier'>SunTracer</b>](https://github.com/mvtea/sgl/tree/master/suntracer).

I chose to transition to a new project after developing SunTracer, and the deconvolutional methods for these images are being worked on by other, more qualified parties, namely Dr. Slava Turyshev and Dr. Victor T. Toth at JPL; interested parties may read the SGL group's [NIAC Final Report](https://arxiv.org/pdf/2002.11871.pdf) (for which they [recently recieved Phase III funding](https://www.nasa.gov/press-release/nasa-selects-early-stage-technology-concepts-for-new-continued-study). Or, for a lighter read, [my paper](https://mvtea.github.io/files/tea_knac2019.pdf) from my talk on the subject at KNAC in fall of 2019.

| ![erf.png](https://mvtea.github.io/files/erf.png) | 
|:--:| 
| *Images of a habitable planet as seen by the SGL.* Here, I utilized RGB data from NASA’s EPIC camera aboard the DSCOVR satellite as the source for SunTracer, which warped the image into an Einstein ring. (*M. V. Tea*)|
