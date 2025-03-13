<?php

namespace App\Repository;

use App\Entity\TraceabilityLog;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<TraceabilityLog>
 */
class TraceabilityLogRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, TraceabilityLog::class);
    }

    // Example of custom methods you could add
    // Find traceability logs for a specific product
    public function findByProductId(int $productId): array
    {
        return $this->createQueryBuilder('t')
            ->andWhere('t.product = :productId')
            ->setParameter('productId', $productId)
            ->orderBy('t.timestamp', 'ASC')
            ->getQuery()
            ->getResult();
    }

    // Find traceability logs by sensor
    public function findBySensorId(int $sensorId): array
    {
        return $this->createQueryBuilder('t')
            ->andWhere('t.sensor = :sensorId')
            ->setParameter('sensorId', $sensorId)
            ->orderBy('t.timestamp', 'ASC')
            ->getQuery()
            ->getResult();
    }

    // Example of a custom method to get logs by event description
    public function findByEventDescription(string $description): array
    {
        return $this->createQueryBuilder('t')
            ->andWhere('t.event_description LIKE :description')
            ->setParameter('description', '%' . $description . '%')
            ->orderBy('t.timestamp', 'ASC')
            ->getQuery()
            ->getResult();
    }
}
