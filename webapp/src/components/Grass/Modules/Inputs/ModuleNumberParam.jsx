/*
 * Filename: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp/src/components/Grass/Modules/Inputs/ModuleNumberParam.jsx
 * Path: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp
 * Created Date: Monday, April 25th 2022, 3:25:56 pm
 * Author: Corey White
 * 
 * Copyright (c) 2022 Corey White
 */


// react
import React, { useState, useEffect, useId } from 'react';


import '../module.scss';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import Form from 'react-bootstrap/Form'
import Map from "../../../OpenLayers/Map"
import Layers from "../../../OpenLayers/Layers/Layers"
import osm from "../../../OpenLayers/Sources/osm"
import TileLayer from "../../../OpenLayers/Layers/TileLayer"
import ModuleCoordsParam from "./ModuleCoordsParam"

const ModuleNumberParam = ({param}) => {

    const [subtype, setSubtype] = useState(null);
    const [defaultOption, setDefaultOption] = useState(null);
    const [subtypeComponent, setSubtypeComponent] = useState(null)
    console.log('ModuleNumberParam')

  
    useEffect(() => {
       
        if (!param) return;
        if (param.schema.type !== 'number') {
            return console.error(`GRASS module parameter ${param.name} is not a number`, param)
        }
        if (param.schema.hasOwnProperty('subtype')) {
            setSubtype(param.schema.subtype)
        }

        if (param.hasOwnProperty('default')) {
            setDefaultOption(param.default)
        }
    }, [param, subtype, defaultOption ])
  

    useEffect(() => {
        if (!subtype) return null;
        if (subtype === 'coords') return setSubtypeComponent(<ModuleCoordsParam param={param} />);
      }, [param, subtype])
    
  
    return (      
        <Form.Group as={Row} controlId={`moduleNumber.${param.name}`} className="mb-3">
            
            <Form.Label column sm={4}>{param.name}</Form.Label>
            <Form.Text muted>{param.description}</Form.Text>
            <Col sm={10}>
                {
                    subtype ? subtypeComponent :
                    <Form.Control 
                        type="number" 
                        placeholder={param.schema.type} 
                    />
                }
            </Col>
        </Form.Group>                  
    )
}


export default ModuleNumberParam




