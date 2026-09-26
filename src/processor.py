#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proyecto: Radar de la Esperanza (Recuperación o Rescate de Vida)
Autor: Aragón López Agustín Christian
Fecha: 25 de septiembre de 2026
Módulo: Filtro de Kalman y Análisis Espectral para detección de signos vitales
"""

import numpy as np

class SignalProcessor:
    def __init__(self, process_variance=1e-3, measurement_variance=1e-1):
        self.Q = process_variance
        self.R = measurement_variance
        self.x_hat = 0.0
        self.P = 1.0

    def kalman_update(self, measurement):
        """Filtro de Kalman discreto para limpiar ruido de alta frecuencia en RSSI."""
        P_pred = self.P + self.Q
        K = P_pred / (P_pred + self.R)
        self.x_hat = self.x_hat + K * (measurement - self.x_hat)
        self.P = (1 - K) * P_pred
        return self.x_hat
