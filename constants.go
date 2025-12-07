package universe

// Fundamental constants - set at the Big Bang, immutable forever
const (
    // Physical constants
    SpeedOfLight       float64 = 299792458       // m/s
    GravitationalConst float64 = 6.67430e-11     // m³/(kg·s²)
    PlanckConstant     float64 = 6.62607015e-34  // J·Hz⁻¹
    BoltzmannConstant  float64 = 1.380649e-23    // J/K
    ElementaryCharge   float64 = 1.602176634e-19 // C
    
    // Universe parameters
    UniverseSeed       int64   = 1765085002          // RNG seed for this timeline
    BigBangCommit      int64   = 1               // The first commit
    
    // Cosmological parameters
    HubbleConstant     float64 = 70.0            // km/s/Mpc
    DarkEnergyFraction float64 = 0.68
    DarkMatterFraction float64 = 0.27
    BaryonicFraction   float64 = 0.05
)

// Current state - updated by the engine
var (
    CosmicAgeMyr float64 = 0  // Millions of years since Big Bang
)
