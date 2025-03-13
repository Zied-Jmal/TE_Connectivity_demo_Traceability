<?php
// src/Entity/Sensor.php
namespace App\Entity;

use ApiPlatform\Core\Annotation\ApiResource;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ApiResource()
 * @ORM\Entity(repositoryClass="App\Repository\SensorRepository")
 */
class Sensor
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $sensor_id;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $sensor_type;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $status;

    // Getters and setters for each property...

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getSensorId(): ?string
    {
        return $this->sensor_id;
    }

    public function setSensorId(string $sensor_id): self
    {
        $this->sensor_id = $sensor_id;
        return $this;
    }

    public function getSensorType(): ?string
    {
        return $this->sensor_type;
    }

    public function setSensorType(string $sensor_type): self
    {
        $this->sensor_type = $sensor_type;
        return $this;
    }

    public function getStatus(): ?string
    {
        return $this->status;
    }

    public function setStatus(string $status): self
    {
        $this->status = $status;
        return $this;
    }
}
