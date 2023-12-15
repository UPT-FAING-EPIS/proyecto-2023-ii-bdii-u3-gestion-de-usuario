[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FQNqnBju)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12894315&assignment_repo_type=AssignmentRepo)

# Desarrollo de un Sistema de Gestión de Usuario con Redis y Flask

Este repositorio contiene el código fuente y la documentación del proyecto "Desarrollo de un Sistema de Gestión de Usuario en el dominio Configuración usando Base de Datos no relacional Redis en el lenguaje PYTHON", desarrollado como parte del curso de Base de Datos II en la Universidad Privada de Tacna.

## Resumen

El proyecto se centra en la creación de un sistema de gestión de usuarios utilizando el framework Flask y un API desarrollado en Python. Este sistema permite a un administrador crear roles y permisos, así como gestionar la creación y actualización de usuarios. Los permisos desempeñan un papel crucial en la asignación de capacidades a los usuarios, proporcionando un control eficiente y seguro sobre los recursos y funcionalidades del sistema mediante el uso de la base de datos no relacional Redis.

## Abstract

This project presents the development of a user management system using the Flask framework and our API created in the Python language. An administrator can create roles and permissions to proceed to create users. Both the created user and the admin will be able to use the profile update feature and view the list of users. These permissions play a fundamental role in assigning the capabilities that users will be able to carry out in the system, providing efficient and secure control over the resources and functionality of the system.

## 1. Introducción

El objetivo principal de este proyecto es desarrollar una API eficiente para la gestión de usuarios, aprovechando tecnologías contemporáneas como bases de datos no relacionales, específicamente Redis, y el servicio Amazon Key Management Services (KMS). La implementación se realiza mediante el framework Flask en conjunto con el lenguaje de programación Python.

La API permitirá a los administradores definir roles y permisos, simplificando la administración de cuentas de usuario. La combinación de Redis para el almacenamiento de datos no relacionales y Amazon KMS para la gestión segura de claves contribuirá a la robustez y seguridad del sistema.

## 2. Título

"Desarrollo de un Sistema de Gestión de Usuario en el dominio Configuración usando Base de Datos no relacional Redis en el lenguaje PYTHON"

## 3. Autores

- Chambe Torres, Edgard Reynaldo
- Nina Vargas, Luigui Augusto
- Condori Vargas, Tomas Yoel
- Sebastian Arce Bracamonte

## 4. Planteamiento del Problema

### 4.1 Problema

La falta de una solución integral puede llevar a la ineficiencia en la administración de cuentas de usuario y a la falta de control sobre los recursos y funcionalidades del sistema.

### 4.2 Justificación

La justificación radica en la necesidad de contar con una API robusta y moderna para la gestión de usuarios combinando Flask, Python, Redis y Amazon KMS, ofreciendo una solución integral que aborda eficiencia en el manejo de datos y seguridad en la gestión de claves.

### 4.3 Alcance

El proyecto se limita al desarrollo de una API para la gestión de usuarios utilizando Flask y Python, con gestión segura de claves mediante Amazon KMS.

## 5. Objetivos

### 5.1 General

Desarrollar una API eficiente para la gestión de usuarios, utilizando tecnologías contemporáneas para la administración de cuentas de usuario y seguridad en la gestión de claves.

### 5.2 Específicos

- Utilizar Redis para el almacenamiento eficiente de datos de usuario.
- Integrar Amazon KMS para una gestión segura de claves.
- Simplificar tareas administrativas mediante procesos automatizados.

## 6. Desarrollo de la Propuesta

### 6.1 Caso de Uso API

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/ef08a15f-0af9-405a-99db-083d18192717)


### 6.2 Diagrama de Clases

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/1b2413f8-fa94-4a06-9ccf-680cfce45115)


### 6.3 Diagrama de Arquitectura

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/cfa59f3c-0f09-475d-bea5-f2997cb6bff5)


### 6.4 Diagrama de Componentes

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/a9eab504-6570-4750-bc98-6691589fa621)


### 6.5 Diagrama de Base de Datos

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/aad2b9e2-d024-43cd-92ae-7c8c10cf7a88)


## 7. Bibliografía

- [ORM Explicación](https://codigofacilito.com/articulos/orm-explicacion)
- [Documentación de Redis en Python](https://redis.io/docs/connect/clients/python/)
- [Redis-py Documentation](https://redis-py.readthedocs.io/en/stable/)

## 8. Anexos

### 8.1 Diccionario de Datos de la Base de Datos Relacional

**Tabla: User**

![image](https://github.com/UPT-FAING-EPIS/proyecto-2023-ii-bdii-u3-gestion-de-usuario/assets/102675967/e901a3d9-bee2-4686-b33e-13f0b502c86a)

