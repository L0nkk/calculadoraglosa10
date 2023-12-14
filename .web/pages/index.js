import { Fragment, useCallback, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "focus-visible/dist/focus-visible"
import { Badge, Box, Button, Center, Divider, Flex, Heading, HStack, Image, Input, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, option, Select, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import dynamic from "next/dynamic"
import NextHead from "next/head"

const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });


export default function Component() {
  const form_state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  const ref_nombre_ep = useRef(null); refs['ref_nombre_ep'] = ref_nombre_ep;
  const ref_valor_terreno = useRef(null); refs['ref_valor_terreno'] = ref_valor_terreno;
  const ref_area_terreno = useRef(null); refs['ref_area_terreno'] = ref_area_terreno;
  const ref_nombre_proyecto = useRef(null); refs['ref_nombre_proyecto'] = ref_nombre_proyecto;
  
    const handleSubmityyenoqln = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{"num_familias": getRefValue(ref_num_familias), "nombre_proyecto": getRefValue(ref_nombre_proyecto), "nombre_ep": getRefValue(ref_nombre_ep), "valor_terreno": getRefValue(ref_valor_terreno), "codigo_proyecto": getRefValue(ref_codigo_proyecto), "area_terreno": getRefValue(ref_area_terreno)}}

        addEvents([Event("form_state.handle_submit", {form_data:form_data})])

        if (false) {
            $form.reset()
        }
    })
    
  const ref_codigo_proyecto = useRef(null); refs['ref_codigo_proyecto'] = ref_codigo_proyecto;
  const ref_num_familias = useRef(null); refs['ref_num_familias'] = ref_num_familias;

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Center>
  <VStack sx={{"paddingTop": "7em", "width": "100%"}}>
  <Box sx={{"position": "fixed", "width": "100%", "top": "0px", "zIndex": "500"}}>
  <HStack justify={`space-between`} sx={{"borderBottom": "0.2em solid #F0F0F0", "paddingX": "2em", "paddingY": "1em", "bg": "rgba(255,255,255, 0.97)"}}>
  <HStack>
  <Image src={`/favicon.ico`} sx={{"width": "50px"}}/>
  <Heading>
  {`Calculadora Glosa 10 SERVIU RM`}
</Heading>
  <Flex>
  <Badge colorScheme={`blue`}>
  {`Dpto. Estudios`}
</Badge>
</Flex>
</HStack>
  <Menu>
  <MenuButton sx={{"bg": "black", "color": "white", "borderRadius": "md", "px": 4, "py": 2}}>
  {`Menu`}
</MenuButton>
  <MenuList>
  <Link as={NextLink} href={`/`}>
  <MenuItem>
  {`INICIO`}
</MenuItem>
</Link>
  <MenuDivider/>
</MenuList>
</Menu>
</HStack>
</Box>
  <VStack sx={{"width": "100%"}}>
  <Text sx={{"fontSize": "2em"}}>
  {`Ingrese los datos del proyecto.`}
</Text>
  <Box as={`form`} onSubmit={handleSubmityyenoqln}>
  <HStack spacing={`2em`}>
  <VStack>
  <Input id={`nombre_ep`} placeholder={`Entidad Solicitante`} ref={ref_nombre_ep} type={`text`}/>
  <Input id={`nombre_proyecto`} placeholder={`Nombre del Proyecto`} ref={ref_nombre_proyecto} type={`text`}/>
  <Input id={`codigo_proyecto`} placeholder={`Código del Proyecto`} ref={ref_codigo_proyecto} type={`text`}/>
</VStack>
  <VStack>
  <Input id={`num_familias`} placeholder={`Número de Familias`} ref={ref_num_familias} type={`text`}/>
  <Select id={`area_terreno`} placeholder={`Seleccione un Área`} ref={ref_area_terreno}>
  <option value={`Area 1`}>
  {`Area 1`}
</option>
  <option value={`Area 2`}>
  {`Area 2`}
</option>
</Select>
  <Input id={`valor_terreno`} placeholder={`Valor del Terreno (UF) (Sin puntos)`} ref={ref_valor_terreno} type={`text`}/>
</VStack>
</HStack>
  <VStack sx={{"paddingTop": "1em"}}>
  <Button type={`submit`}>
  {`Calcular!`}
</Button>
</VStack>
</Box>
</VStack>
  <Divider/>
  <VStack>
  <Heading>
  {`Resultados`}
</Heading>
  <HStack spacing={`5em`} sx={{"paddingTop": "1em"}}>
  <VStack>
  <Heading size={`lg`}>
  {`Familias con mas de 40% RSH`}
</Heading>
  <HStack>
  <Text>
  {`Valor Terreno por Familia:`}
</Text>
  <Text>
  {form_state.results_mas40.at(0)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Inicial:`}
</Text>
  <Text>
  {form_state.results_mas40.at(1)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Base:`}
</Text>
  <Text>
  {form_state.results_mas40.at(2)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro mas Subsidio:`}
</Text>
  <Text>
  {form_state.results_mas40.at(3)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Saldo del Terreno:`}
</Text>
  <Text>
  {form_state.results_mas40.at(4)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`%:`}
</Text>
  <Text>
  {form_state.results_mas40.at(5)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Adicional:`}
</Text>
  <Text>
  {form_state.results_mas40.at(6)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Adicional:`}
</Text>
  <Text>
  {form_state.results_mas40.at(7)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Total:`}
</Text>
  <Text>
  {form_state.results_mas40.at(8)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Terreno Total:`}
</Text>
  <Text>
  {form_state.results_mas40.at(9)}
</Text>
</HStack>
</VStack>
  <VStack>
  <Heading size={`lg`}>
  {`Familias con menos de 40% RSH`}
</Heading>
  <HStack>
  <Text>
  {`Valor Terreno por Familia:`}
</Text>
  <Text>
  {form_state.results_menos40.at(0)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Inicial:`}
</Text>
  <Text>
  {form_state.results_menos40.at(1)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Base:`}
</Text>
  <Text>
  {form_state.results_menos40.at(2)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro mas Subsidio:`}
</Text>
  <Text>
  {form_state.results_menos40.at(3)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Saldo del Terreno:`}
</Text>
  <Text>
  {form_state.results_menos40.at(4)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`%:`}
</Text>
  <Text>
  {form_state.results_menos40.at(5)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Adicional:`}
</Text>
  <Text>
  {form_state.results_menos40.at(6)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Adicional:`}
</Text>
  <Text>
  {form_state.results_menos40.at(7)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Ahorro Total:`}
</Text>
  <Text>
  {form_state.results_menos40.at(8)}
</Text>
</HStack>
  <HStack>
  <Text>
  {`Subsidio Terreno Total:`}
</Text>
  <Text>
  {form_state.results_menos40.at(9)}
</Text>
</HStack>
</VStack>
</HStack>
</VStack>
  <Divider/>
  <VStack>
  <Heading>
  {`Analisis de Sensibilidad de Variables`}
</Heading>
  <Heading size={`md`}>
  {`Num Familias (Eje X) VS Ahorro UF (Eje Y)`}
</Heading>
  <Heading size={`sm`}>
  {`Cada categoría es un valor de terreno diferente`}
</Heading>
  <Plot data={form_state.scat_fig} layout={{"width": "1000", "height": "600"}}/>
</VStack>
</VStack>
</Center>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
