---
permalink: /research/
title: "Research"
excerpt: "About me"
author_profile: true
redirect_from: 
---


# Characterizing accreting binaries in the local universe with *Chandra* (*Spring 2020 - Present*)

Observations of X-ray radiation from nearby galaxies provide the best opportunities to study the some of the universe’s most extreme environments, neutron stars (NSs) and black holes (BHs) interacting with stars in binary systems in particular. Emission from these X-ray binaries (XRBs) allows us to study the effects of compact objects on their environment and the physics evolved in their emission.

XRBs are known to exist in distinct X-ray emission states related directly to their mass accretion rate; sources cycle through these states over time, and observing a full cycle would allow us to determine the nature of the compact object as either a NS or BH. Professor Kilgard’s group has been working on a complete census of XRBs in the local universe, a sample comprised of more than 45,000 individual sources. However, the timescales for emission cycles for XRBs can range from days to decades, making analysis difficult for large samples of objects.

For this reason, I have conducted a detailed spectro-temporal analysis on a small subset of these sources, namely the 78 most luminous sources in the sample. For each of these sources, I have made rough determinations of X-ray spectral state and performed timing analysis to search for and characterize variability. Of the sources included in the sample, 15 are suspected serendipitous observations of previously unstudied objects for which I provide a preliminary classification. 

I have identified 5 of these sources of special interest for follow-up, exhibiting signs of either quasiperiodicity, transitionary X-ray states or active accretion events. Over the course of my final year at Wesleyan, I'll be performing additional analysis on the sources of interest aforementioned, culminating in my honors thesis. Stay tuned.


# Raytracing the Solar Gravitational Lens (SGL) with Python (*Fall 2017 - Spring 2019*)

Gravitational lensing is a phenomenon wherein a massive object, like a galaxy or cluster of galaxies, bends the trajectory of light of a bright source located behind it, which we observe on Earth as a warping or duplication of the source on the sky. If the conditions are just right and the source, lens and observer are perfectly aligned (*in syzygy*), what we observe is called an Einstein ring, a circle of light about the limb of the lens containing highly-magnified light from the source; this alignment rarely occurs in nature.

Strong lensing is only seen occuring around very massive bodies from here on Earth, but this is simply due to the fact that the mass of a given gravitational lens is dependant on the distance from its gravitational focus. That is to say, gravitational lensing can occur for any size object, but all low-mass objects (like stars) are too far from the Earth for it to be at their gravitational focus. The Sun, even, has a gravitational focus at a minimum of ~550AU - it is this fact that the Solar Gravitational Lens (SGL) seeks to take advantage of.

The SGL is a theoretical space telescope comprised of a modest meter-class telescope pointed at the Sun (outfitted with a coronograph, of course) and placed at its gravitational focus. When aligned in syzygy with a target exoplanet, the resulting Einstein ring will contain highly-magnified, extreme-resolution data from the surface of the exoplanet. With the optical properties of the SGL, this is essentially equivalent to a sattelite orbiting Earth taking an image of the state of Connecticut.

From the first few weeks of my time as an undergraduate in 2017 to the end of the summer of 2019, I worked with Professor Seth Redfield on simulating the images we might see from the SGL once it is positioned, so that we may begin work on a reconstruction algorithm for converting the warped light from the Einstein rings it gathers back into an image of the source's surface. This project culminated in a general-relativistic raytracing algorithm I call [<b style='font: courier'>SunTracer</b>](https://github.com/mvtea/sgl/tree/master/suntracer).

I chose transition to a new project after developing SunTracer, and the deconvolutional methods for these images are being worked on by other, more qualified parties, namely Dr. Slava Turyshev and Dr. Victor T. Toth at JPL; interested parties may read the SGL group's [NIAC Final Report](https://arxiv.org/pdf/2002.11871.pdf) (for which they [recently recieved Phase III funding](https://www.nasa.gov/press-release/nasa-selects-early-stage-technology-concepts-for-new-continued-study). Or, for a lighter read, [my paper](https://mvtea.github.io/files/tea_knac2019.pdf) from my talk on the subject at KNAC in fall of 2019.

| ![erf.png](https://mvtea.github.io/files/erf.png) | 
|:--:| 
| *Images of a habitable planet as seen by the SGL.* Here, I utilized RGB data from NASA’s EPIC camera aboard the DSCOVR satellite as the source for SunTracer, which warped the image into an Einstein ring. |
