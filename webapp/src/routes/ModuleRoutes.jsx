/*
 * Filename: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp/src/routes/ModuleRoutes.jsx
 * Path: /home/coreywhite/Documents/GitHub/TomorrowNow/TomorrowNowApp/webapp
 * Created Date: Friday, April 22nd 2022, 12:17:08 pm
 * Author: Corey White
 * 
 * Copyright (c) 2022 Corey White
 */


import React, { Fragment} from "react"

import { Route } from "react-router-dom";
import ModulesContainer from '../containers/Modules/ModulesContainer';
import Module from "../components/Grass/Modules/Module";
import Modules from "../components/Grass/Modules/Modules";
// import ModuleFamily from "../components/Grass/Modules/ModuleFamily";

const ModuleRouters = (
  <Fragment>
    <Route path="modules" element={<ModulesContainer /> }>
      <Route path=":familyName" element={<Modules /> }>
        <Route path=":moduleName" element={<Module /> } />
      </Route>
    </Route>
    {/* <Route path="modules/:familyName/:moduleName" element={<Module /> } /> */}
  </Fragment>
)

export default ModuleRouters