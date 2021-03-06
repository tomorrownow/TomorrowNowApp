/*
 * Filename: useActiniaAsyncProcess.js
 * Project: TomorrowNow
 * File Created: Thursday May 19th 2022
 * Author: Corey White (smortopahri@gmail.com)
 * Maintainer: Corey White
 * -----
 * Last Modified: Thu May 19 2022
 * Modified By: Corey White
 * -----
 * License: GPLv3
 * 
 * Copyright (c) 2022 TomorrowNow
 * 
 * TomorrowNow is an open-source geospatial participartory modeling platform
 * to enable stakeholder engagment in socio-environmental decision-makeing.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 * 
 */

import React, {useState, useEffect} from 'react';
import useWebSocket, { ReadyState } from 'react-use-websocket';
const ACTINIA_SOCKET_URL = 'ws://localhost:8005/ws/savana/resource/'

export const useActiniaAsyncProcess = ({status, resourceId}) => {
    const [socketUrl, setSocketUrl] = useState(null); // pending...
    const [messageHistory, setMessageHistory] = useState(['test']);
    const { sendMessage, lastMessage, lastJsonMessage, readyState, getWebSocket } = useWebSocket(socketUrl, { share: false });
    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
      }[readyState];

    // Open Websocket Connention for resource
    useEffect(()=> {
        if (!resourceId || !status) return;
        console.log("Starting Websocket...")
        console.log("Websocket: ResourceId Received...")
        console.log(`Websocket: Resource Id: ${resourceId}`)
        let resourceName = resourceId.replace(/-/g , '_')
        console.log(`Websocket: Resource Name: ${resourceName}`)
        setSocketUrl( `${ACTINIA_SOCKET_URL}${resourceName}/`)
    },[status, resourceId])

    // Send websocket status message to server
    useEffect(()=> {
        if (readyState != ReadyState.OPEN) return;
        console.log("Sending Websocket Message: ", status)
        sendMessage(JSON.stringify({message: status, resource_id: resourceId}))
        setMessageHistory([{message: status, resource_id: resourceId}])
    },[connectionStatus])

    // Log last message from Websocket
    useEffect(()=> {
        if (readyState != ReadyState.OPEN) return;
        console.log("Last Websocket Message", lastMessage)
    },[lastMessage])

    // Get Websocket message history
    useEffect(() => {
        if (lastMessage !== null) {
            setMessageHistory((prev) => prev.concat(lastMessage));
        }
    }, [lastMessage]);

    // Set source data once data is finished
    useEffect(() => {
        if (!lastJsonMessage) return;
        console.log("Last Message: ", lastJsonMessage)
        console.log("Last Message Finished: ", lastJsonMessage)
    }, [lastJsonMessage])

    return {lastJsonMessage, messageHistory, wsState: readyState}

    
}