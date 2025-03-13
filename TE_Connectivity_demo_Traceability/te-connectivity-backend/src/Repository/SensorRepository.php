<?php

namespace App\Repository;

use App\Entity\Sensor;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Sensor>
 */
class SensorRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Sensor::class);
    }

    // Example of custom methods you could add
    // Find a sensor by its sensor_id
    public function findBySensorId(string $sensorId): ?Sensor
    {
        return $this->createQueryBuilder('s')
            ->andWhere('s.sensor_id = :sensorId')
            ->setParameter('sensorId', $sensorId)
            ->getQuery()
            ->getOneOrNullResult();
    }

    // Find all sensors with a specific status
    public function findByStatus(string $status): array
    {
        return $this->createQueryBuilder('s')
            ->andWhere('s.status = :status')
            ->setParameter('status', $status)
            ->orderBy('s.id', 'ASC')
            ->getQuery()
            ->getResult();
    }
}
