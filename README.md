[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FQNqnBju)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12894315&assignment_repo_type=AssignmentRepo)

# Desarrollo de un Sistema de Gestión de Usuario con Redis y Flask

Este repositorio contiene el código fuente y la documentación del proyecto "Desarrollo de un Sistema de Gestión de Usuario en el dominio Configuración usando Base de Datos no relacional Redis en el lenguaje PYTHON", desarrollado como parte del curso de Base de Datos II en la Universidad Privada de Tacna.

## Resumen

Este proyecto se propone desarrollar una API eficiente para la gestión de usuarios, haciendo uso de tecnologías contemporáneas como Redis y MySQL para almacenar datos no relacionales y relacionales, respectivamente. La implementación se lleva a cabo con Flask y Python, integrando Amazon Key Management Services (KMS) para asegurar una gestión segura de claves. La API permitirá a los administradores definir roles y permisos, simplificando la administración de cuentas de usuario y optimizando la eficiencia del sistema. Se aborda la falta de una solución integral para la gestión de usuarios, y se busca ofrecer una solución completa y moderna que garantice robustez y seguridad.

## Abstract

This project aims to develop an efficient API for user management, making use of contemporary technologies such as Redis and MySQL to store non-relational and relational data, respectively. The implementation is carried out with Flask and Python, integrating Amazon Key Management Services (KMS) to ensure secure key management. The API will allow administrators to define roles and permissions, simplifying user account management and optimizing system efficiency. The lack of a comprehensive solution for user management is addressed, and the aim is to offer a complete and modern solution that guarantees robustness and security.

## 1. Introducción

Este proyecto tiene como objetivo principal desarrollar una API eficiente para la gestión de usuarios, utilizando tecnologías contemporáneas como bases de datos no relacionales, en este caso, Redis, y bases de datos relacionales, específicamente MySQL, junto con el servicio de gestión de claves Amazon Key Management Services (KMS). La implementación se lleva a cabo mediante el framework Flask en conjunto con el lenguaje de programación Python.
En este contexto, la API permitirá a los administradores definir roles y permisos, simplificando la administración de cuentas de usuario. La combinación de Redis para el almacenamiento de datos no relacionales, MySQL para la gestión de datos relacionales y Amazon KMS para la gestión segura de claves contribuirá a la robustez y seguridad del sistema. Los principios de Flask facilitarán el desarrollo ágil y la creación de endpoints eficientes.
Este proyecto busca ofrecer una solución completa y moderna para la gestión de usuarios a través de una API, aprovechando la sinergia entre Redis, MySQL, Amazon KMS, Flask y Python en el proceso.	

## 2. Título

 "Desarrollo de un Sistema de Gestión de Usuario en el dominio Configuración"

## 3. Autores

- Chambe Torres, Edgard Reynaldo
- Nina Vargas, Luigui Augusto
- Condori Vargas, Tomas Yoel
- Sebastian Arce Bracamonte

## 4. Planteamiento del Problema

### 4.1 Problema

El problema abordado en este proyecto es la falta de una solución integral puede llevar a la ineficiencia en la administración de cuentas de usuario y a la falta de control sobre los recursos y funcionalidades del sistema.

### 4.2 Justificación

Este proyecto surge de la necesidad de desarrollar una API robusta para la gestión de usuarios. Se utiliza el framework Flask con Python, combinando bases de datos no relacionales como Redis y bases de datos relacionales como MySQL. Además, se implementa Amazon Key Management Services (KMS) para asegurar una gestión segura de claves. La integración de estas tecnologías busca ofrecer una solución completa y moderna que optimice la eficiencia en el manejo de datos y garantice la seguridad en la gestión de claves, abordando así los requisitos esenciales del proyecto.

### 4.3 Alcance

El alcance de este proyecto se extiende al desarrollo de una API integral para la gestión de usuarios mediante el uso de Flask y Python. Se incluirá la implementación segura de claves a través de Amazon KMS. El sistema final, respaldado por esta API, posibilitará a los usuarios, ya sean administradores o usuarios regulares, acceder a perfiles y visualizar listas de usuarios. Además, se contemplará la capacidad de gestionar roles y permisos para los administradores, proporcionando una funcionalidad más completa y adaptada a las necesidades de la gestión de usuarios.

## 5. Objetivos

### 5.1 General

El objetivo general de este proyecto es desarrollar una API eficiente para la gestión de usuarios, utilizando estas tecnologías contemporáneas brindando una solución completa para la administración de cuentas de usuario y a la vez seguridad en la gestión de claves.

### 5.2 Específicos

- Utilizar Redis como base de datos no relacional para el  almacenamiento eficiente de datos de usuario.
- Integrar Amazon KMS para una gestión segura de claves, garantizando la seguridad de la información.
- Simplificar las tareas administrativas mediante procesos automatizados. 

## 7. Desarrollo de la Propuesta

### 7.1 Caso de Uso API

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/33a5955c-d04b-43bc-bc6e-d1806e02aee0)

### 7.2 Diagrama de Clases

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/d2e5da53-a921-49d1-8380-4d09f36b0744)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/11bf6501-437c-4901-9803-8bfdcbf47732)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/d25c42ed-5158-4569-b031-a99e5ebd41d5)

### 7.3 Diagrama de Arquitectura

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/f5072a57-ee6b-49ed-86e4-4b4d97eae730)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/243e7c66-e1f0-444e-bfed-463fe9f369e5)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/b8e185bd-8732-4d66-8dfd-61e436426268)

### 7.4 Diagrama de Componentes

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/d45fd962-2f9b-41ad-b989-a3ef7680905a)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/425de965-37fe-4d0c-a6a6-e29ab72d4947)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/775c6fac-76e3-4e87-80c1-d09eeb45ab00)

### 7.5 Diagrama de Base de Datos

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/55ff80dc-d0f7-4184-b582-13e9bd48d7b9)
![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/1fe87c6c-bd4b-4e43-bcd9-bd2530c4243f)

## 8. Concluciones

En conclusión, la integración de Flask, Redis y MySQL en la creación de una API para la gestión de usuarios ofrece una solución equilibrada y eficiente. 
Flask proporciona agilidad en el desarrollo, Redis garantiza un almacenamiento rápido y versátil para datos no relacionales, y MySQL aporta estructura para datos relacionales. 
La inclusión de Amazon KMS refuerza la seguridad en la gestión de claves. En conjunto, estas tecnologías forman una API completa y moderna que cumple con los requisitos de rendimiento, seguridad y eficiencia en la gestión de usuarios.	


## 9. Bibliografía

https://codigofacilito.com/articulos/orm-explicacion 
https://redis.io/docs/connect/clients/python/
https://redis-py.readthedocs.io/en/stable/		
https://github.com/features/actions
https://dev.to/msnmongare/title-building-a-food-api-with-django-and-mysql-5b12
https://docs.docker.com/engine/api/
https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/patterns/run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance.html	
