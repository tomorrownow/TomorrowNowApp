/*
 * Filename: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp/src/components/Grass/Utils/GrassRenderImage.jsx
 * Path: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp
 * Created Date: Thursday, April 28th 2022, 5:44:35 pm
 * Author: Corey White
 * 
 * Copyright (c) 2022 Corey White
 */

import React, { useState, useEffect } from "react"
import Spinner from "react-bootstrap/Spinner"
import Grass from "../grass";
import Card from "react-bootstrap/Card"
import Image from "react-bootstrap/Image"


const GrassRenderImage = ({layerType, layerName, mapsetName, locationName, card=true}) => {
    const [image, setImage] = useState(null)
    const [loading, setLoading] = useState(true)
    // useDataSource
    useEffect(() => {
        if (!layerType || !layerName || !mapsetName || !locationName) return;
        let isMounted = true; 
        (async () => {
            // if (!isMounted) return null;
            try {
                let data = null;
                if (layerType === 'raster') {
                    data = await Grass.d.renderRaster(locationName, mapsetName, layerName)
                }
                if (layerType === 'vector') {
                    data = await Grass.d.renderVector(locationName, mapsetName, layerName)
                }
                
                data.response.imgurl = `data:image/png;base64,${data.response.imagedata}`
                const layerImage = data.response
                setImage(layerImage)
               
                setLoading(false)
              } catch (e) {
                console.log(e);
            }
            return () => { isMounted = false }
          })()
         
      },[layerType, layerName, mapsetName, locationName])

     
      return (
        <>
            {
                loading ? 
                <Spinner as="span" animation="border" role="status" variant="secondary" className="bg-dark text-light" >
                    <span className="visually-hidden">Loading...</span>
                </Spinner>
                :
                card ? <Card.Img as="img" variant="top" src={image ? image.imgurl : ""} className="bg-dark text-light"/> :
                <Image as="img" fluid={true} src={image ? image.imgurl : ""} className="bg-dark text-light"></Image>
            }
        </>
      )

};

export default GrassRenderImage