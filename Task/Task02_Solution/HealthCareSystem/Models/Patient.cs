using System;
using System.Collections.Generic;

namespace HealthCareSystem.Models
{
    public class Patient
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime DateOfBirth { get; set; }

        // Navigation Property: Many-to-Many with Doctor (via Appointment)
        public ICollection<Appointment> Appointments { get; set; } = new HashSet<Appointment>();
    }
}
