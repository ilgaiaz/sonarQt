import numpy as np

class KalmanFilter(object):
    def __init__(self, F = None, B = None, H = None, Q = None, R = None, P = None, x0 = None):

        if(F is None or H is None):
            raise ValueError("Set proper system dynamics.")

        self.n = F.shape[1]
        self.m = H.shape[1]
        #State-transition model
        self.F = F
        #Observation model
        self.H = H
        #Control-input model which is applied to the control vector u
        self.B = 0 if B is None else B
        #Covariance of the process noise
        self.Q = np.eye(self.n) if Q is None else Q
        #Covariance of the observation noise
        self.R = np.eye(self.n) if R is None else R
        #Predicted error convariance
        self.P = np.eye(self.n) if P is None else P
        #State predicted 
        self.x = np.zeros((self.n, 1)) if x0 is None else x0

    def predict(self, u = 0):
        #Predicted (a priori) state estimate x(heat)=F*x(heat)+B*u
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        #Predicted (a priori) error covariance P= FxPxF(trasposed)+Q
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x

    def update(self, z):
        #y = z - Hx
        y = z - np.dot(self.H, self.x)
        #S = R + H*P*H(traposed)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))
        #K = P*H(transposed) * S^-1
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.n)
        #P = ((I-K*H)*P)*(I-K*H)(transposed) + K*R*K(transposed)
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P), 
        	(I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R), K.T)

    def predicted_state(self, u=0):
        return np.dot(self.H, self.predict(u))

def example():
    dt = 1.0/60
    F = np.array([[1, dt, 0], [0, 1, dt], [0, 0, 1]])
    H = np.array([1, 0, 0]).reshape(1, 3)
    Q = np.array([[0.05, 0.05, 0.0], [0.05, 0.05, 0.0], [0.0, 0.0, 0.0]])
    R = np.array([0.5]).reshape(1, 1)

    x = np.linspace(-10, 10, 100)
    measurements = - (x**2 + 2*x - 2)  + np.random.normal(0, 2, 100)

    kf = KalmanFilter(F = F, H = H, Q = Q, R = R)
    predictions = []

    for z in measurements:
        predictions.append(kf.predicted_state()[0])
        kf.update(z)

    import matplotlib.pyplot as plt
    plt.plot(range(len(measurements)), measurements, label = 'Measurements')
    plt.plot(range(len(predictions)), np.array(predictions), label = 'Kalman Filter Prediction')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    example()
