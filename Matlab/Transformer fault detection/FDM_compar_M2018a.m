% Programación de los métodos basados en variables eléctricas para la
% detección de fallas en transformadores.
%
% María del Pilar Buitrago-Villada, 2024
%
%   - El transformador a evaluar en todos los métodos será monofásico.
%   - Las simplificaciones asumidas son
clc
%% Lectura de datos desde el archivo suministrado por Rymel S.A.S.
fprintf('-----------------------------------------------\n')
fprintf('Lectura de la base de datos \n.')
fprintf('-----------------------------------------------\n')

V1 = 7620;
V2 = 240;

%registros a leer debe empezar en 2, el 1 corresponde al encabezado. 
i_trx = (2:4); 

%inicialización de estructuras de datos
I1 = zeros(length(i_trx),1);
I2 = zeros(length(i_trx),1);
Rp1 = zeros(length(i_trx),1);
Rs1 = zeros(length(i_trx),1);

cont = 1;
for i = i_trx
    
% El encabezado ocupa las fila 1 a 4. Sumar 4 al registro del id
    range = strcat('A',string(i),':','I',string(i));

% leer todo el registro
    [data, txt, raw] = xlsread('NewBD_MATLAB.xlsx', range);

% Corrientes nominales, primario (1) y secundario (2)
    I1(cont) = raw{1};
    I2(cont) = raw{2};

% Resistencia de los devanados, primario (p) y secundario (s)
    Rp1(cont) = raw{3};
    Rs1(cont) = raw{4};
    
    cont = cont+1;
end

% Relación de transformación
% TR = cell2mat(raw(39));

%% Lectura de datos de las hojas Datos de prueba Trafo #1 y #2
% Corriente en el primario
%I1_m2 = [xlsread('NewBD_MATLAB.xlsx','Datos de prueba Trafo #1','F22:F27');
%         xlsread('NewBD_MATLAB.xlsx','Datos de prueba Trafo #2','F22:F27')];

% Corriente en el secundario
%I2_m2 = [xlsread('NewBD_MATLAB.xlsx','Datos de prueba Trafo #1','I22:I27');
%         xlsread('NewBD_MATLAB.xlsx','Datos de prueba Trafo #2','I22:I27')];


%% Lectura de datos de una hoja específica seleccionada por el usuario
% Solicitar al usuario el nombre de la hoja
sheet_name = input('Ingrese el nombre de la hoja de datos del transformador #1: ', 's');
sheet_name1 = input('Ingrese el nombre de la hoja de datos del transformador #2: ', 's');

% Corriente en el primario
I1_m2 = [xlsread('NewBD_MATLAB.xlsx',sheet_name,'F22:F27');
         xlsread('NewBD_MATLAB.xlsx',sheet_name1,'F22:F27')];

%I1_m2 = [xlsread('NewBD_MATLAB.xlsx',sheet_name,'F22:F27')];

% Corriente en el secundario
%I2_m2 = [xlsread('NewBD_MATLAB.xlsx',sheet_name,'F22:F27')];

I2_m2 = [xlsread('NewBD_MATLAB.xlsx',sheet_name,'I22:I27');
         xlsread('NewBD_MATLAB.xlsx',sheet_name1,'I22:I27')];

%% Método 1: Sensado de corrientes diferenciales (Bhide et al., 2014)
fprintf('Método de solución 1: Sensado de corrientes diferenciales (Bhide et al., 2014)\n')

% Datos de entrada del método 1
% I1_cal    Corrientes de calibración medidas en el primario
% I2_cal    Corrientes de calibración medidas en el secundario   
% I1, I2    Corrientes de fase en el primario y secundario, respectivamente
% Idiff     Corriente diferencial
% TR        Relación de transformación
% Eallow    Error permisible

Eallow = 0.2;

% -------------------------------------------------------------------------
% 1. Modo de calibración
% -------------------------------------------------------------------------
fprintf('\t ... Inicio del modo de calibración.\n')

% Procesamiento de los de tres puntos de carga
% I1, I2 tienen que ser vectores de 3x1
I1_cal = I1;
I2_cal = I2;

y = I1_cal./I2_cal;
x = 1./I2_cal;
p = polyfit(x,y,1); %ajuste lineal a los datos

Idiff = p(1); % coeficiente de x (pendiente de la recta)
N2_N1 = p(2); % término independiente

% -------------------------------------------------------------------------
% 2. Modo de monitorización
% -------------------------------------------------------------------------
% tomar I1 e I2 d elas hojas Datos de prueba Trafo #1 y #2
fprintf('\t ... Inicio del modo de monitorización.\n')

m = size(I1_m2);

for j = 1: m
    Idiff_prim = I1_m2 - N2_N1.*I2_m2;

    if (Idiff_prim > Idiff)
        Err = abs(Idiff - Idiff_prim); % cálculo de la severidad de la falla
    
        if Err > Eallow
            fprintf('\t Alarma de falla en el transformador. \n')
        end
    else
        %vuelve al lazo para evaluar otro valor de corriente (si existe)
    end
end
fprintf('-----------------------------------------------\n')

%% Método 2: Estimación de corrientes de correlación (Etumi & Anayi, 2016)
fprintf('Método de solución 2: Estimación de corrientes de correlación (Etumi & Anayi, 2016)\n')

% Datos de entrada del método 2
% n     Número de ventanas de muestreo
% m     Número de muestras por ventana de correlación
% I1    Vector de mediciones de corriente en el primario para los m 
%       instantes de muestreo. Ingresarlo como vector columna.
% I2    Vector de mediciones de corriente en el secundario para los m 
%       instantes de muestreo. Ingresarlo como vector columna
% U     Umbral para la determinación de la ocurrencia de una falla

U = 0.9; %tomado del artículo

% NOTAS: En I1_m2 e I2_m2 se juntan las corrientes medidas en las hojas  
% Datos de prueba trafo #1 y #2. Cada prueba sería una ventana de muestreo

m = 6; %seis puntos de carga

% ventanas de muestreo
n = 2;

% inicialización de los vectores de coeficientes de correlación cruzada y
% auto correlación
R11 = zeros(n-1);
R22 = zeros(n-1);
R12 = zeros(n);

% corrientes de la ventana n = 1
i1_prev = I1_m2(1:m);
i2_prev = I2_m2(1:m);
c = m;

% calculo del coeficiente de correlación para n = 1
R12(1) = FDM_correlation_coef(i1_prev,i2_prev); 

for i = 2:n
% -------------------------------------------------------------------------   
% leer/adquirir el valor de I1 e I2 para la ventana actual i
% -------------------------------------------------------------------------
    i1 = I1_m2(c+1:i*m);
    i2 = I2_m2(c+1:i*m);
    c = i*m;
% -------------------------------------------------------------------------    
% Calcular los coeficientes de correlación R11, R22 y R12
% -------------------------------------------------------------------------
% coeficiente de auto-correlación
% Los coeficientes de autocorrelación Rii se calculan entre ventanas de 
% muestras de corriente consigo mismas pero desplazadas en un ciclo, 
% es decir, ventanas de un ciclo con ventanas del anterior.
% -------------------------------------------------------------------------
    R11(i-1) = FDM_correlation_coef(i1,i1_prev); 
    R22(i-1) = FDM_correlation_coef(i2,i2_prev);   
% -------------------------------------------------------------------------
% coeficiente de correlación cruzada entre las corrientes del primario y
% del secundario (por fase)
% -------------------------------------------------------------------------
    R12(i) = FDM_correlation_coef(i1,i2);
    
% en la siguiente iteración, la ventana actual pasa a ser la ventana previa
    i1_prev = i1;
    i2_prev = i2;
end
fprintf('\t Coeficientes de correlación: \n')
fprintf('\t \t R11 = %2.4f\n',R11)
fprintf('\t \t R22 = %2.4f\n',R22)
fprintf('\t Coeficientes de correlación cruzada: \n')
fprintf('\t \t R12 = %2.4f\n',R12)
% ------------------------------------------------------------------------- 
% Determinación de la alerta
% ------------------------------------------------------------------------- 
if(any(R11<U) & any(R22<U) & any(R12<U) | any(R12<U))
    fprintf('Método 2: Falla interna\n')
    fprintf('Fin\n')
else
    for j = 1:n-1
        if(R11(j)<U && R22(j)<U && R12(j+1)>U) 
            fprintf('\t Falla externa con saturación de TC.\n')
        else
            if(R11(j)<U && R22(j)<U && all(R12>0.9))
                fprintf('\t Falla externa con saturación de dos TCs idénticos.\n')
            else
                fprintf('\t Operación normal.\n')
            end           
        end
    end
end
fprintf('-----------------------------------------------\n')

%% Método 3: Diferencia de corrientes entre devanados sano y defectuoso (Aburaghiega et al., 2018)

% Datos de entrada del método 3
% I1h   Vector de corrientes de devanado primario sano
% I2h   Vector de corrientes de devanado secundario sano
% I1f   Vector de corrientes de devanado primario cuando hay falla
% I2f   Vector de corrientes de devanado secundario cuando hay falla

% Determinación de los coeficientes de las ecuaciones que definen Ish y
% Iarc

% Determinación del número de espiras en falla

% Cálculo de la corriente de corto circuito Ish

% Cálculo de la corriente Iarc