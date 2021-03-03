---
permalink: /research/
title: "Research"
excerpt: "About me"
author_profile: true
redirect_from: 
---


# Characterizing accreting binaries in the local universe with *Chandra* (*Spring 2020 - Present*)

Not only do half of all stars exist in binary systems, but roughly 70% of all stars with a mass in excess of 10 solar masses reside in binaries. This makes it unsurprising that compact objects, namely neutron stars and black holes, are most often found in binary systems, as these >10$M_\odot$ stars are fated to become one of the two when they die. These binaries, comprised of one of the aforementioned compact objects and a companion star, emit X-rays from a super-hot accretion disk of material that has been ripped away from the companion and siphoned into orbit around the compact object, radiating at high energies as it loses gravitational energy on its spiral inward.
  
Observations of these X-ray binaries (XRBs) provide the best opportunities to study some of the universe's most extreme environments, including the physics invloved in the strong gravity of these compact objects and high-energy plasma physics in their accretion disks. Of particular interest in my research are black hole X-ray binaries (BHXRBs), which are known to exist in distinct X-ray emission states related directly to their mass accretion rate. Sources cycle through these states over time, and observing a full cycle would allow us to determine the nature of the compact object as either a neutron star or a black hole. However, the timescales of these cycles range from days to decades, prohibiting detailed analysis of large samples of sources.

Our group has been working on a complete census of X-ray sources in galaxies within 15 megaparsecs, a sample including ~45,000 individual sources extracted from archival _Chandra_ observations spanning from its launch to May of 2016. I have imposed on this sample a lower limit of 2,000 counts, yielding a sample of ~80 sources which, with appropriate binning, allow for statistically significant differentiation between unique spectral models. On this much smaller sample, I have been working alongside [Professor Roy Kilgard](http://rkilgard.faculty.wesleyan.edu/) to (a) provide preliminary determinations of X-ray spectral state for each of the sources, (b) perform additional analysis on sources exhibiting behavior indicative of variability, quasiperiodicity, and/or X-ray spectral state transitions, and (c) interpret the results of this population of XRBs as it pertains to the initial sample, possibly constraining further the parameter space for local XRBs.

This work will culminate in my honors thesis in astronomy in Spring 2021. Please see my [Presentations page](https://mvtea.github.io/presentations/) for more info.

| ![BHB](https://images.ctfassets.net/cnu0m8re1exe/5BIngirakRnX3gIKHE3c2M/63905ab53aa5b2b8cf3f1fa5b4013f94/bhbinary_xmm_960.jpg?w=650&h=433&fit=fill) | 
|:--:| 
| *An artist's rendition of the HMXB Cyg-X1, one of the first discovered and most well-studied XRBs. (Credit: NASA, CXC, M. Weiss)* |

<br/><br/>

# Raytracing the Solar Gravitational Lens (SGL) with Python (*Fall 2017 - Spring 2019*)

Gravitational lensing is a phenomenon wherein a massive object, like a galaxy or cluster of galaxies, bends the trajectory of light of a bright source located behind it, which we observe on Earth as a warping or duplication of the source image on the sky. If the conditions are just right and the source, lensing object and observer are perfectly aligned (*in syzygy*), what we observe is called an Einstein ring, a circle of light about the limb of the lens containing highly-magnified light from the source. This alignment, however, rarely occurs in nature.

Strong lensing is only seen occuring around very massive bodies from here on Earth, but this is simply due to the fact that the mass of a given gravitational lens is dependent on the distance from its gravitational focus. That is to say, gravitational lensing can occur for any size object, but all low-mass objects (like stars) are too far from the Earth for us to be at their gravitational focus. The Sun, even, has a gravitational focus at a minimum of ~550AU, and it is this fact that the Solar Gravitational Lens (SGL) seeks to take advantage of.

The SGL is a theoretical space telescope comprised of a meter-class telescope outfitted with a coronagraph, pointed at the Sun, and placed at its gravitational focus. When aligned in syzygy with a target exoplanet, the resulting Einstein ring will contain highly-magnified, extreme-resolution data from the surface of the exoplanet. With the optical properties of the SGL, this is essentially equivalent to a sattelite orbiting Earth taking an image of the state of Connecticut.

From the first few weeks of my time as an undergraduate in 2017 to the end of the summer of 2019, I worked with [Professor Seth Redfield](https://sethredfield.wescreates.wesleyan.edu/) on simulating the images we might see from the SGL once it is positioned, so that we may begin work on a reconstruction algorithm for converting the warped light from the Einstein rings that it gathers back into an image of the source's surface. This project culminated in a general-relativistic raytracing algorithm I call [<b style='font: courier'>SunTracer</b>](https://github.com/mvtea/sgl/tree/master/suntracer).

I chose to transition to a new project after developing SunTracer, and the deconvolutional methods for these images are being worked on by other, more qualified parties, namely Dr. Slava Turyshev and Dr. Victor T. Toth at JPL; interested parties may read the SGL group's [NIAC Final Report](https://arxiv.org/pdf/2002.11871.pdf) (for which they [recently recieved Phase III funding](https://www.nasa.gov/press-release/nasa-selects-early-stage-technology-concepts-for-new-continued-study). Or, for a lighter read, [my paper](https://mvtea.github.io/files/tea_knac2019.pdf) from my talk on the subject at KNAC in fall of 2019. Please see my [Presentations page](https://mvtea.github.io/presentations/) for more info.

| ![erf.png](https://mvtea.github.io/files/erf.png) | 
|:--:| 
| *Images of a habitable planet as seen by the SGL.* Here, I utilized RGB data from NASA’s EPIC camera aboard the DSCOVR satellite as the source for SunTracer, which warped the image into an Einstein ring. |
